from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import procedures_dao


class ProceduresService(GeneralService):
    _dao = procedures_dao

    def get_statistics_from_procedures_price(self, stat_type):
        return self._dao.get_statistics_from_procedures_price(stat_type)
