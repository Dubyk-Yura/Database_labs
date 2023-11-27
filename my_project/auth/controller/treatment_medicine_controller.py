from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import treatment_schemes_service


class TreatmentMedicineController(GeneralController):
    _service = treatment_schemes_service

    def find_by_treatment_id(self, treatment_id: int):
        return self._service.find_by_treatment_id(treatment_id)

    def find_by_medicine_id(self, medicine_id: int):
        return self._service.find_by_medicine_id(medicine_id)
