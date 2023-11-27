from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import pet_dao


class PetService(GeneralService):
    _dao = pet_dao

    def get_clients_for_pet(self, pet_id: int):
        return self._dao.get_clients_for_pet(pet_id)

    def get_diagnoses_for_pet(self, pet_id: int):
        return self._dao.get_diagnoses_for_pet(pet_id)
