from typing import Dict, List, Any

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Diagnoses, Pet, pet_diagnoses


class DiagnosesDAO(GeneralDAO):
    _domain_type = Diagnoses

    def get_pets_for_diagnoses(self, diagnoses_id: int) -> dict[str, list[Any] | Any]:
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
        pets = session.query(Pet).filter(Pet.id.in_(pet_ids)).all()
        diagnoses = session.query(Diagnoses).filter_by(id=diagnoses_id).first()
        data = {
            "diagnoses": diagnoses.put_into_dto(),
            "pets": [pet.put_into_dto() for pet in pets]
        }
        return data

    def connect_pet_and_diagnoses_from_diagnoses(self, diagnoses_id: int, pet_id: int):
        session = self.get_session()
        session.execute(pet_diagnoses.insert().values(diagnoses_id=diagnoses_id, pet_id=pet_id))
        session.commit()
