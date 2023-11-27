from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import medicine_procedures_schemes_dao


class MedicineProceduresSchemesService(GeneralService):
    _dao = medicine_procedures_schemes_dao
