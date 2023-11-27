from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import medicine_dao


class MedicineService(GeneralService):
    _dao = medicine_dao

    def find_by_name(self, name: str):
        return self._dao.find_by_name(name)


