from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import client_dao


class ClientService(GeneralService):
    _dao = client_dao

    def get_pets_for_client(self, client_id: int):
        return self._dao.get_pets_for_client(client_id)

    def get_services_for_client(self, client_id: int):
        return self._dao.get_services_for_client(client_id)
