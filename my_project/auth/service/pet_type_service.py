from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import pet_type_dao


class PetTypeService(GeneralService):
    _dao = pet_type_dao

    def insert_ten_rows_into_pet_type(self):
        return self._dao.insert_ten_rows_into_pet_type()

    def insert_in_pet_type(self, new_type: str):
        return self._dao.insert_in_pet_type(new_type)
