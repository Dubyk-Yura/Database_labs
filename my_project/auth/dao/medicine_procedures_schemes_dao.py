from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import MedicineProceduresSchemes


class MedicineProceduresSchemesDAO(GeneralDAO):
    _domain_type = MedicineProceduresSchemes
