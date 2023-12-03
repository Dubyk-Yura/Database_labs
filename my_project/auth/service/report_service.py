from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import report_dao


class ReportService(GeneralService):
    _dao = report_dao
