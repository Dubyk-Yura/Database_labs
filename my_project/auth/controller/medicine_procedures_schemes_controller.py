from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import medicine_procedures_schemes_service


class MedicineProceduresSchemesController(GeneralController):
    _service = medicine_procedures_schemes_service

    def find_by_medicine_id(self, medicine_id: int):
        return self._service.find_by_medicine_id(medicine_id)
