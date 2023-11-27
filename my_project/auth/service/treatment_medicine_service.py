from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import treatment_medicine_dao


class TreatmentMedicineService(GeneralService):
    _dao = treatment_medicine_dao

    def find_by_treatment_id(self, treatment_id: int):
        return self._dao.find_by_treatment_id(treatment_id)

    def find_by_medicine_id(self, medicine_id: int):
        return self._dao.find_by_medicine_id(medicine_id)
