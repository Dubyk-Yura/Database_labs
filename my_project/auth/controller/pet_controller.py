from my_project.auth.service import pet_service
from my_project.auth.controller.general_controller import GeneralController


class PetController(GeneralController):
    _service = pet_service

    def get_clients_for_pet(self, pet_id: int):
        return self._service.get_clients_for_pet(pet_id)

    def get_diagnoses_for_pet(self, pet_id: int):
        return self._service.get_diagnoses_for_pet(pet_id)

    def connect_pet_and_client_from_pet(self, pet_id: int, client_id: int):
        self._service.connect_pet_and_client_from_pet(pet_id, client_id)

    def connect_pet_and_diagnoses_from_pet(self, pet_id: int, diagnoses_id: int):
        self._service.connect_pet_and_diagnoses_from_pet(pet_id, diagnoses_id)

    def remove_client_from_pet(self, pet_id: int, client_id: int):
        self._service.remove_client_from_pet(pet_id, client_id)

    def remove_diagnoses_from_pet(self, pet_id: int, client_id: int):
        self._service.remove_diagnoses_from_pet(pet_id, client_id)
