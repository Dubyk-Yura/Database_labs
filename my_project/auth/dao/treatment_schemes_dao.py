from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import TreatmentSchemes


class TreatmentSchemesDAO(GeneralDAO):
    _domain_type = TreatmentSchemes
