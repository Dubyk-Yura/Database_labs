from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Treatment


class TreatmentDAO(GeneralDAO):
    _domain_type = Treatment

    def find_by_diagnoses_id(self, diagnoses_id: int) -> list[object]:
        """
        Gets object from database table by integer key.
        :param diagnoses_id: integer key (surrogate primary key)
        :return: search object
        """
        return self._session.query(self._domain_type).get(diagnoses_id)
