from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import medicine_dao


class MedicineService(GeneralService):
    _dao = medicine_dao
