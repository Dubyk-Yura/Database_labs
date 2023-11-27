from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Services, ScheduledVisit, Client


class ServicesDAO(GeneralDAO):
    _domain_type = Services

    def get_clients_for_service(self, service_id: int) -> list[Client]:
        """
        Gets all clients for a specific service by service's ID.
        :param service_id: ID of the client
        :return: list of clients associated with the client
        """
        session = self.get_session()
        client_ids = (
            session.query(ScheduledVisit.client_id)
            .filter(ScheduledVisit.services_id == service_id).all()
        )
        client_ids = [client_id for (client_id,) in client_ids]
        clients = session.query(Client).filter(Client.id.in_(client_ids)).all()
        return [client.put_into_dto() for client in clients]
