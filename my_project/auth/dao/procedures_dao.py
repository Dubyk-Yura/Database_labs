from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Procedures


class ProceduresDAO(GeneralDAO):
    _domain_type = Procedures

    def find_by_name(self, name: str) -> list[object]:
        """
        Gets Status objects from database table by field status.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Procedures).filter(Procedures.name == name).order_by(Procedures.name).all()
