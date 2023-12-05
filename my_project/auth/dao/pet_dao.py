from typing import Any

from sqlalchemy import text

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Client, client_pet, Pet, Diagnoses, pet_diagnoses


class PetDAO(GeneralDAO):
    _domain_type = Pet

    def get_clients_for_pet(self, pet_id: int) -> dict[str, list[Any] | Any]:
        """
        Gets all clients for a specific pet by pet's ID.
        :param pet_id: ID of the pet
        :return: list of client associated with the pet
        """
        session = self.get_session()
        client_ids = (
            session.query(client_pet.c.client_Id)
            .filter(client_pet.c.pet_id == pet_id).all()
        )
        client_ids = [client_id for (client_id,) in client_ids]
        clients = session.query(Client).filter(Client.id.in_(client_ids)).all()
        pet = session.query(Pet).filter_by(id=pet_id).first()
        data = {
            "pet": pet.put_into_dto(),
            "clients": [client.put_into_dto() for client in clients]
        }
        return data

    def get_diagnoses_for_pet(self, pet_id: int) -> dict[str, list[Any] | Any]:
        """
        Gets all diagnoses for a specific pet by pet's ID.
        :param pet_id: ID of the pet
        :return: list of diagnoses associated with the pet
        """
        session = self.get_session()
        diagnoses_ids = (
            session.query(pet_diagnoses.c.diagnoses_id)
            .filter(pet_diagnoses.c.pet_id == pet_id).all()
        )
        diagnoses_ids = [diagnoses_id for (diagnoses_id,) in diagnoses_ids]
        clients = session.query(Diagnoses).filter(Diagnoses.id.in_(diagnoses_ids)).all()
        pet = session.query(Pet).filter_by(id=pet_id).first()
        data = {
            "pet": pet.put_into_dto(),
            "diagnoses": [diagnoses.put_into_dto() for diagnoses in clients]
        }
        return data

    def connect_pet_and_client_from_pet(self, pet_id: int, client_id: int):
        session = self.get_session()
        session.execute(client_pet.insert().values(client_Id=client_id, pet_id=pet_id))
        session.commit()

    def connect_pet_and_diagnoses_from_pet(self, pet_id: int, diagnoses_id: int):
        session = self.get_session()
        session.execute(pet_diagnoses.insert().values(diagnoses_id=diagnoses_id, pet_id=pet_id))
        session.commit()

    def remove_client_from_pet(self, pet_id: int, client_id: int):
        session = self.get_session()
        session.execute(
            client_pet.delete()
            .where(client_pet.c.client_Id == client_id)
            .where(client_pet.c.pet_id == pet_id)
        )
        session.commit()

    def remove_diagnoses_from_pet(self, pet_id: int, diagnoses_id: int):
        session = self.get_session()
        session.execute(
            pet_diagnoses.delete()
            .where(pet_diagnoses.c.diagnoses_id == diagnoses_id)
            .where(pet_diagnoses.c.pet_id == pet_id)
        )
        session.commit()

    def insert_in_client_pet_by_values(self, client_name: str, client_surname: str, client_contact_number: str,
                                       pet_name: str, pet_age: int):
        try:
            session = self.get_session()
            sql_expression = text("call insert_in_client_pet_by_values(:client_name, :client_surname,"
                                  ":client_contact_number, :pet_name, :pet_age)")
            session.execute(sql_expression,
                            {'client_name': client_name,
                             'client_surname': client_surname,
                             'client_contact_number': client_contact_number,
                             'pet_name': pet_name,
                             'pet_age': pet_age,
                             })
            session.commit()
        except Exception as e:
            print(f"Error inserting in client pet: {e}")

