from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import diagnoses_dao


class DiagnosesService(GeneralService):
    _dao = diagnoses_dao

    def find_by_name(self, name: str):
        return self._dao.find_by_name(name)

    def get_pets_for_diagnoses(self, diagnoses_id: int):
        return self._dao.get_pets_for_diagnoses(diagnoses_id)



