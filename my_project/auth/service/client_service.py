from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import client_dao


class ClientService(GeneralService):
    _dao = client_dao

    def get_pets_for_client(self, client_id: int):
        return self._dao.get_pets_for_client(client_id)

    def get_services_for_client(self, client_id: int):
        return self._dao.get_services_for_client(client_id)

    def connect_pet_and_client_from_client(self, client_id: int, pet_id: int):
        self._dao.connect_pet_and_client_from_client(client_id, pet_id)

    def remove_pet_from_client(self, client_id: int, pet_id: int):
        self._dao.remove_pet_from_client(client_id, pet_id)
