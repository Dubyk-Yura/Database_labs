from my_project.auth.service import medicine_service
from my_project.auth.controller.general_controller import GeneralController


class MedicineController(GeneralController):
    _service = medicine_service

    def find_by_name(self, name: str):
        return self._service.find_by_name(name)
