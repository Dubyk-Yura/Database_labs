from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Client, client_pet, Pet, Diagnoses, pet_diagnoses


class PetDAO(GeneralDAO):
    _domain_type = Pet

    def find_by_pet_type_id(self, pet_type_id: int) -> list[object]:
        """
        Gets object from database table by integer key.
        :param pet_type_id: integer key (surrogate primary key)
        :return: search object
        """
        return self._session.query(self._domain_type).get(pet_type_id)

    def get_clients_for_pet(self, pet_id: int) -> list[Client]:
        """
        Gets all clients for a specific pet by pet's ID.
        :param pet_id: ID of the pet
        :return: list of client associated with the pet
        """
        session = self.get_session()
        client_ids = (
            session.query(client_pet.c.client_id)
            .filter(client_pet.c.pet_id == pet_id).all()
        )
        client_ids = [client_id for (client_id,) in client_ids]
        clients = session.query(Pet).filter(Pet.id.in_(client_ids)).all()
        return [client.put_into_dto() for client in clients]

    def get_diagnoses_for_pet(self, pet_id: int) -> list[Diagnoses]:
        """
        Gets all diagnoses for a specific pet by pet's ID.
        :param pet_id: ID of the pet
        :return: list of diagnoses associated with the pet
        """
        session = self.get_session()
        diagnoses_ids = (
            session.query(pet_diagnoses.c.client_id)
            .filter(pet_diagnoses.c.pet_id == pet_id).all()
        )
        diagnoses_ids = [diagnoses_id for (diagnoses_id,) in diagnoses_ids]
        clients = session.query(Pet).filter(Pet.id.in_(diagnoses_ids)).all()
        return [diagnoses.put_into_dto() for diagnoses in clients]
