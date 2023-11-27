from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class TreatmentSchemes(db.Model, IDto):
    __tablename__ = "treatment_schemes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(45), nullable=False)

    # Relationship 1:M
    medicine_procedures_schemes = db.relationship("MedicineProceduresSchemes", backref="treatment_schemes_",
                                                  uselist=False)

    def __repr__(self) -> str:
        return f"TreatmentSchemes({self.id}, '{self.name}', '{self.description}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> TreatmentSchemes:
        obj = TreatmentSchemes(
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
        )
        return obj
