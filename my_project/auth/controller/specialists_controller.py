from my_project.auth.service import specialists_service
from my_project.auth.controller.general_controller import GeneralController


class SpecialistsController(GeneralController):
    _service = specialists_service
