from my_project.auth.service import diagnoses_service
from my_project.auth.controller.general_controller import GeneralController


class DiagnosesController(GeneralController):
    _service = diagnoses_service

    def get_pets_for_diagnoses(self, diagnoses_id: int):
        return self._service.get_pets_for_diagnoses(diagnoses_id)

    def connect_pet_and_diagnoses_from_diagnoses(self, diagnoses_id: int, pet_id: int):
        return self._service.connect_pet_and_diagnoses_from_diagnoses(diagnoses_id, pet_id)

    def remove_pet_from_diagnoses(self, diagnoses_id: int, pet_id: int):
        return self._service.remove_pet_from_diagnoses(diagnoses_id, pet_id)
