from my_project.auth.service import pet_type_service
from my_project.auth.controller.general_controller import GeneralController


class PetTypeController(GeneralController):
    _service = pet_type_service

    def insert_ten_rows_into_pet_type(self):
        return self._service.insert_ten_rows_into_pet_type()

    def insert_in_pet_type(self, new_type: str):
        return self._service.insert_in_pet_type(new_type)
