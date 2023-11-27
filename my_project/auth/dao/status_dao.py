from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Status


class StatusDAO(GeneralDAO):
    _domain_type = Status
