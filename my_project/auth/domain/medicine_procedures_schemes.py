from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class MedicineProceduresSchemes(db.Model, IDto):
    __tablename__ = "medicine_procedures_schemes"

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    # ForeignKey
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'), primary_key=True, nullable=False)
    treatment_schemes_id = db.Column(db.Integer, db.ForeignKey('treatment_schemes.id'), primary_key=True,
                                     nullable=False)
    procedures_id = db.Column(db.Integer, db.ForeignKey('procedures.id'), primary_key=True, nullable=False)

    # Relationship 1:M
    medicine = db.relationship("Medicine", backref="medicine_procedures_schemes_")
    treatment_schemes = db.relationship("TreatmentSchemes", backref="medicine_procedures_schemes_")
    procedures = db.relationship("Procedures", backref="medicine_procedures_schemes_")

    def __repr__(self) -> str:
        return f"MedicineProceduresSchemes({self.id}, '{self.medicine_id}', '{self.treatment_schemes_id}'," \
               f" '{self.procedures_id}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "medicine_id": self.medicine_id,
            "treatment_schemes_id": self.treatment_schemes_id,
            "procedures_id": self.procedures_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> MedicineProceduresSchemes:
        obj = MedicineProceduresSchemes(
            id=dto_dict.get("id"),
            medicine_id=dto_dict.get("medicine_id"),
            treatment_schemes_id=dto_dict.get("treatment_schemes_id"),
            procedures_id=dto_dict.get("procedures_id")
        )
        return obj
