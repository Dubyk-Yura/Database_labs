from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Procedures(db.Model, IDto):
    __tablename__ = "procedures"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    schedule = db.Column(db.String(45), nullable=True)
    description = db.Column(db.String(150), nullable=True)

    # Relationship 1:M
    medicine_procedures_schemes = db.relationship("MedicineProceduresSchemes", backref="procedures_", uselist=False)

    def __repr__(self) -> str:
        return f"Procedures({self.id}, '{self.name}', '{self.price}', '{self.schedule}', '{self.description}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "schedule": self.schedule,
            "description": self.description,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Procedures:
        obj = Procedures(
            name=dto_dict.get("name"),
            price=dto_dict.get("price"),
            schedule=dto_dict.get("schedule"),
            description=dto_dict.get("description"),
        )
        return obj
