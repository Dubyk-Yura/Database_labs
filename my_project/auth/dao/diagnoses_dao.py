from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Diagnoses, Pet, pet_diagnoses


class DiagnosesDAO(GeneralDAO):
    _domain_type = Diagnoses

    def find_by_name(self, name: str) -> list[object]:
        """
        Gets Status objects from database table by field status.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Diagnoses).filter(Diagnoses.name == name).order_by(Diagnoses.name).all()

    def get_pets_for_diagnoses(self, diagnoses_id: int) -> list[Pet]:
        """
        Gets all pets for a specific diagnoses by diagnoses ID.
        :param diagnoses_id: ID of the diagnoses
        :return: list of client associated with the pet
        """
        session = self.get_session()
        pet_ids = (
            session.query(pet_diagnoses.c.pet_id)
            .filter(pet_diagnoses.c.diagnoses_id == diagnoses_id).all()
        )
        pet_ids = [pet_id for (pet_id,) in pet_ids]
        clients = session.query(Pet).filter(Pet.id.in_(pet_ids)).all()
        return [client.put_into_dto() for client in clients]
