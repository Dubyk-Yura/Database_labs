from my_project.auth.service import report_service
from my_project.auth.controller.general_controller import GeneralController


class ReportController(GeneralController):
    _service = report_service

