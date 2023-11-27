from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import pet_type_dao


class PetTypeService(GeneralService):
    _dao = pet_type_dao
