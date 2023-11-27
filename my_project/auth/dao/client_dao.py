from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Client, client_pet, Pet, ScheduledVisit, Services


class ClientDAO(GeneralDAO):
    _domain_type = Client

    def get_pets_for_client(self, client_id: int) -> list[Pet]:
        """
        Gets all pets for a specific client by client's ID.
        :param client_id: ID of the client
        :return: list of pets associated with the client
        """
        session = self.get_session()
        pet_ids = (
            session.query(client_pet.c.pet_id)
            .filter(client_pet.c.client_Id == client_id).all()
        )
        pet_ids = [pet_id for (pet_id,) in pet_ids]
        pets = session.query(Pet).filter(Pet.id.in_(pet_ids)).all()
        return [pet.put_into_dto() for pet in pets]

    def get_services_for_client(self, client_id: int) -> list[Services]:
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
        return [serv.put_into_dto() for serv in services]
