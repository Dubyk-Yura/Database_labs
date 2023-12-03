from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Report


class ReportDAO(GeneralDAO):
    _domain_type = Report
