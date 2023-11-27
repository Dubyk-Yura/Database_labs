from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import status_dao


class StatusService(GeneralService):
    _dao = status_dao
