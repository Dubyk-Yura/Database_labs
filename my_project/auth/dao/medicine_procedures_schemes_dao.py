from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import MedicineProceduresSchemes


class MedicineProceduresSchemesDAO(GeneralDAO):
    _domain_type = MedicineProceduresSchemes

    def find_by_medicine_id(self, medicine_id: int) -> list[object]:
        """
        Gets object from database table by integer key.
        :param medicine_id: integer key (surrogate primary key)
        :return: search object
        """
        return self._session.query(self._domain_type).get(medicine_id)
