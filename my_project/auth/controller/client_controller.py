from my_project.auth.service import client_service
from my_project.auth.controller.general_controller import GeneralController


class ClientController(GeneralController):
    _service = client_service

    def get_pets_for_client(self, client_id: int):
        return self._service.get_pets_for_client(client_id)

    def get_services_for_client(self, client_id: int):
        return self._service.get_services_for_client(client_id)

    def connect_pet_and_client_from_client(self, client_id: int, pet_id: int):
        self._service.connect_pet_and_client_from_client(client_id, pet_id)

    def remove_pet_from_client(self, client_id: int, pet_id: int):
        self._service.remove_pet_from_client(client_id, pet_id)

    def insert_in_client_pet_by_values(self, client_name: str, client_surname: str, client_contact_number: str,
                                       pet_name: str, pet_age: int):
        self._service.insert_in_client_pet_by_values(client_name, client_surname, client_contact_number, pet_name,
                                                     pet_age)
