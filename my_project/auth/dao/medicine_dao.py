from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Medicine


class MedicineDAO(GeneralDAO):
    _domain_type = Medicine
