from my_project.auth.service import procedures_service
from my_project.auth.controller.general_controller import GeneralController


class ProceduresController(GeneralController):
    _service = procedures_service

    def get_statistics_from_procedures_price(self, stat_type):
        return self._service.get_statistics_from_procedures_price(stat_type)
