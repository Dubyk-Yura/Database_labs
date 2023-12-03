from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Treatment


class TreatmentDAO(GeneralDAO):
    _domain_type = Treatment
