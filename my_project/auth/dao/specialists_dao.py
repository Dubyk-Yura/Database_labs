from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Specialists


class SpecialistsDAO(GeneralDAO):
    _domain_type = Specialists

    def find_by_name(self, name: str) -> list[object]:
        """
        Gets Status objects from database table by field status.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Specialists).filter(Specialists.name == name).order_by(Specialists.name).all()
