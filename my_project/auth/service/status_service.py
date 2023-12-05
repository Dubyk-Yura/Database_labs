from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import status_dao


class StatusService(GeneralService):
    _dao = status_dao

    def convert_rows_in_databases(self):
        return self._dao.convert_rows_in_databases()