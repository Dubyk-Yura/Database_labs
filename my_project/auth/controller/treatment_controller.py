from my_project.auth.service import treatment_service
from my_project.auth.controller.general_controller import GeneralController


class TreatmentController(GeneralController):
    _service = treatment_service
