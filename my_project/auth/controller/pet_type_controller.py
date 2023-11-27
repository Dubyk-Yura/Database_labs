from my_project.auth.service import pet_type_service
from my_project.auth.controller.general_controller import GeneralController


class PetTypeController(GeneralController):
    _service = pet_type_service
