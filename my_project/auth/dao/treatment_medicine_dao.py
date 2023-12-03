from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import TreatmentMedicine


class TreatmentMedicineDAO(GeneralDAO):
    _domain_type = TreatmentMedicine
