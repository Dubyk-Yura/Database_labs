from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import specialists_dao


class SpecialistsService(GeneralService):
    _dao = specialists_dao
