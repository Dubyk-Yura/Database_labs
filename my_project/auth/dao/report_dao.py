from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Status


class ReportDAO(GeneralDAO):
    _domain_type = Status
