from my_project.auth.service import status_service
from my_project.auth.controller.general_controller import GeneralController


class StatusController(GeneralController):
    _service = status_service

    def convert_rows_in_databases(self):
        return self._service.convert_rows_in_databases()
