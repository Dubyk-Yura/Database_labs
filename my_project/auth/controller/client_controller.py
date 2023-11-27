from my_project.auth.service import client_service
from my_project.auth.controller.general_controller import GeneralController


class ClientController(GeneralController):
    _service = client_service

    def get_pets_for_client(self, client_id: int):
        return self._service.get_pets_for_client(client_id)

    def get_services_for_client(self, client_id: int):
        return self._service.get_services_for_client(client_id)

