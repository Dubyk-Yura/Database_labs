from typing import Any

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Client, client_pet, Pet, ScheduledVisit, Services
from sqlalchemy import text


class ClientDAO(GeneralDAO):
    _domain_type = Client

    def get_pets_for_client(self, client_id: int) -> dict[str, list[Any] | Any]:
        """
        Gets all pets for a specific client by client's ID.
        :param client_id: ID of the client
        :return: list of pets associated with the client
        """
        session = self.get_session()
        client = session.query(Client).filter_by(id=client_id).first()
        pet_ids = (
            session.query(client_pet.c.pet_id)
            .filter(client_pet.c.client_Id == client_id).all()
        )
        pet_ids = [pet_id for (pet_id,) in pet_ids]
        pets = session.query(Pet).filter(Pet.id.in_(pet_ids)).all()
        data = {
            "client": client.put_into_dto(),
            "pets": [pet.put_into_dto() for pet in pets]
        }
        return data

    def get_services_for_client(self, client_id: int) -> dict[str, list[Any] | Any]:
        """
        Gets all services for a specific client by client's ID.
        :param client_id: ID of the client
        :return: list of services associated with the client
        """
        session = self.get_session()
        service_ids = (
            session.query(ScheduledVisit.services_id)
            .filter(ScheduledVisit.client_id == client_id).all()
        )
        service_ids = [service_id for (service_id,) in service_ids]
        services = session.query(Services).filter(Services.id.in_(service_ids)).all()
        client = session.query(Client).filter_by(id=client_id).first()
        data = {
            "client": client.put_into_dto(),
            "services": [serv.put_into_dto() for serv in services]
        }
        return data

    def connect_pet_and_client_from_client(self, client_id: int, pet_id: int):
        session = self.get_session()
        session.execute(client_pet.insert().values(client_Id=client_id, pet_id=pet_id))
        session.commit()

    def remove_pet_from_client(self, client_id: int, pet_id: int):
        session = self.get_session()
        session.execute(
            client_pet.delete()
            .where(client_pet.c.client_Id == client_id)
            .where(client_pet.c.pet_id == pet_id)
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
