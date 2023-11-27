from my_project.auth.service import procedures_service
from my_project.auth.controller.general_controller import GeneralController


class ProceduresController(GeneralController):
    _service = procedures_service
