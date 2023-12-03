from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import treatment_medicine_dao


class TreatmentMedicineService(GeneralService):
    _dao = treatment_medicine_dao
