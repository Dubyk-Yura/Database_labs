from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import treatment_schemes_dao


class TreatmentSchemesService(GeneralService):
    _dao = treatment_schemes_dao
