from my_project.auth.service import treatment_service
from my_project.auth.controller.general_controller import GeneralController


class TreatmentController(GeneralController):
    _service = treatment_service

    def find_by_diagnoses_id(self, diagnoses_id: int) -> list[object]:
        return self._service.find_by_diagnoses_id(diagnoses_id)
