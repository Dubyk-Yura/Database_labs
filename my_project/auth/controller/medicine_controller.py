from my_project.auth.service import medicine_service
from my_project.auth.controller.general_controller import GeneralController


class MedicineController(GeneralController):
    _service = medicine_service
