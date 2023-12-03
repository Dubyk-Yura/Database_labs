from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import treatment_medicine_service


class TreatmentMedicineController(GeneralController):
    _service = treatment_medicine_service

