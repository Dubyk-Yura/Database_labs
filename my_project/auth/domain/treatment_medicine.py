from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class TreatmentMedicine(db.Model, IDto):
    __tablename__ = "treatment_medicine"

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    # ForeignKey
    treatment_id = db.Column(db.Integer, db.ForeignKey('treatment.id'), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'), primary_key=True, nullable=False)

    # Relationship 1:M
    treatment = db.relationship("Treatment", backref="treatment_medicine_")
    medicine = db.relationship("Medicine", backref="treatment_medicine_")

    def __repr__(self) -> str:
        return f"TreatmentMedicine({self.id}, '{self.name}', '{self.surname}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "treatment_id": self.treatment_id,
            "medicine_id": self.medicine_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> TreatmentMedicine:
        obj = TreatmentMedicine(
            id=dto_dict.get("id"),
            treatment_id=dto_dict.get("treatment_id"),
            medicine_id=dto_dict.get("medicine_id"),
        )
        return obj
