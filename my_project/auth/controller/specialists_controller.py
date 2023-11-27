from my_project.auth.service import specialists_service
from my_project.auth.controller.general_controller import GeneralController


class SpecialistsController(GeneralController):
    _service = specialists_service

    def find_by_name(self, name: str):
        return self._service.find_by_name(name)
