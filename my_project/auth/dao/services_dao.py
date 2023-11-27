from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Services, ScheduledVisit, Client


class ServicesDAO(GeneralDAO):
    _domain_type = Services

    def find_by_specialists_id(self, specialists_id: int) -> list[object]:
        """
        Gets object from database table by integer key.
        :param specialists_id: integer key (surrogate primary key)
        :return: search object
        """
        return self._session.query(self._domain_type).get(specialists_id)

    def get_clients_for_service(self, service_id: int) -> list[Client]:
        """
        Gets all clients for a specific service by service's ID.
        :param service_id: ID of the client
        :return: list of clients associated with the client
        """
        session = self.get_session()
        client_ids = (
            session.query(ScheduledVisit.c.client_id)
            .filter(ScheduledVisit.c.service_id == service_id).all()
        )
        client_ids = [client_id for (client_id,) in client_ids]
        clients = session.query(Client).filter(Client.id.in_(client_ids)).all()
        return [client.put_into_dto() for client in clients]
