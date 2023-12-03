from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import treatment_schemes_service


class TreatmentSchemesController(GeneralController):
    _service = treatment_schemes_service
