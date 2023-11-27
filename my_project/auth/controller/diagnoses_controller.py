from my_project.auth.service import diagnoses_service
from my_project.auth.controller.general_controller import GeneralController


class DiagnosesController(GeneralController):
    _service = diagnoses_service

    def find_by_name(self, name: str):
        return self._service.find_by_name(name)

    def get_pets_for_diagnoses(self, diagnoses_id: int):
        return self._service.get_pets_for_diagnoses(diagnoses_id)
