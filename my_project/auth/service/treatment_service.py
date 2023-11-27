from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import treatment_dao


class TreatmentService(GeneralService):
    _dao = treatment_dao

    def find_by_diagnoses_id(self, diagnoses_id: int) -> list[object]:
        return self._dao.find_by_diagnoses_id(diagnoses_id)
