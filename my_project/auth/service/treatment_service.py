from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import treatment_dao


class TreatmentService(GeneralService):
    _dao = treatment_dao
