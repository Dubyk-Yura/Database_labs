from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import PetType


class PetTypeDAO(GeneralDAO):
    _domain_type = PetType


