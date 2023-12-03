from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Procedures


class ProceduresDAO(GeneralDAO):
    _domain_type = Procedures
