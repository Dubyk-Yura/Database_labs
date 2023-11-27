from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Treatment(db.Model, IDto):
    __tablename__ = "treatment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    schedule = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(150), nullable=True)

    # ForeignKey
    diagnoses_id = db.Column(db.Integer, db.ForeignKey('diagnoses.id'), nullable=False)

    # Relationship 1:M
    diagnoses = db.relationship("Diagnoses", backref="treatment_")
    treatment_medicine = db.relationship("TreatmentMedicine", backref="treatment_")

    def __repr__(self) -> str:
        return f"Treatment({self.id}, '{self.name}', '{self.schedule}', '{self.price}','{self.description}'" \
               f",'{self.diagnoses_id}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "schedule": self.schedule,
            "price": self.price,
            "description": self.description,
            "diagnoses_id": self.diagnoses_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Treatment:
        obj = Treatment(
            name=dto_dict.get("name"),
            schedule=dto_dict.get("schedule"),
            price=dto_dict.get("price"),
            description=dto_dict.get("description"),
            diagnoses_id=dto_dict.get("diagnoses_id"),
        )
        return obj
