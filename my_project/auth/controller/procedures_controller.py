from my_project.auth.service import procedures_service
from my_project.auth.controller.general_controller import GeneralController


class ProceduresController(GeneralController):
    _service = procedures_service

    def find_by_name(self, name: str):
        return self._service.find_by_name(name)
