from my_project.auth.service import pet_service
from my_project.auth.controller.general_controller import GeneralController


class PetController(GeneralController):
    _service = pet_service

    def find_by_pet_type_id(self, pet_type_id: int):
        return self._service.find_by_pet_type_id(pet_type_id)

    def get_clients_for_pet(self, pet_id: int):
        return self._service.get_clients_for_pet(pet_id)

    def get_diagnoses_for_pet(self, pet_id: int):
        return self._service.get_diagnoses_for_pet(pet_id)
