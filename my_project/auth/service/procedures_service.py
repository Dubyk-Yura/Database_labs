from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import procedures_dao


class ProceduresService(GeneralService):
    _dao = procedures_dao

    def find_by_name(self, name: str):
        return self._dao.find_by_name(name)


