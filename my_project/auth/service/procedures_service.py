from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import procedures_dao


class ProceduresService(GeneralService):
    _dao = procedures_dao
