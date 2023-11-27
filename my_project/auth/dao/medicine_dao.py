from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Medicine


class MedicineDAO(GeneralDAO):
    _domain_type = Medicine

    def find_by_name(self, name: str) -> list[object]:
        """
        Gets Status objects from database table by field status.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Medicine).filter(Medicine.name == name).order_by(Medicine.name).all()
