from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import medicine_procedures_schemes_dao


class MedicineProceduresSchemesService(GeneralService):
    _dao = medicine_procedures_schemes_dao

    def find_by_medicine_id(self, medicine_id: int):
        return self._dao.find_by_medicine_id(medicine_id)
