from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import pet_dao


class PetService(GeneralService):
    _dao = pet_dao

    def get_clients_for_pet(self, pet_id: int):
        return self._dao.get_clients_for_pet(pet_id)

    def get_diagnoses_for_pet(self, pet_id: int):
        return self._dao.get_diagnoses_for_pet(pet_id)

    def connect_pet_and_client_from_pet(self, pet_id: int, client_id: int):
        self._dao.connect_pet_and_client_from_pet(pet_id, client_id)

    def connect_pet_and_diagnoses_from_pet(self, pet_id: int, diagnoses_id: int):
        self._dao.connect_pet_and_diagnoses_from_pet(pet_id, diagnoses_id)

    def remove_client_from_pet(self, pet_id: int, client_id: int):
        self._dao.remove_client_from_pet(pet_id, client_id)

    def remove_diagnoses_from_pet(self, pet_id: int, client_id: int):
        self._dao.remove_diagnoses_from_pet(pet_id, client_id)

    def insert_in_client_pet_by_values(self, client_name: str, client_surname: str, client_contact_number: str,
                                       pet_name: str, pet_age: int):
        self._dao.insert_in_client_pet_by_values(client_name, client_surname, client_contact_number, pet_name, pet_age)
