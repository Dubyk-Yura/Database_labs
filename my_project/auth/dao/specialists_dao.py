from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Specialists


class SpecialistsDAO(GeneralDAO):
    _domain_type = Specialists
