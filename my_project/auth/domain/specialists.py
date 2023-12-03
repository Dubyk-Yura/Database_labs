from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Specialists(db.Model, IDto):
    __tablename__ = "specialists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    specialization = db.Column(db.String(45), nullable=False)
    working_hours = db.Column(db.String(45), nullable=True)
    licenses = db.Column(db.String(45), nullable=True)

    # Relationship 1:M
    services = db.relationship("Services", backref="specialists_")

    def __repr__(self) -> str:
        return f"Specialists({self.id}, '{self.name}', '{self.surname}', '{self.specialization}', '{self.working_hours}'," \
               f" '{self.licenses}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "specialization": self.specialization,
            "working_hours": self.working_hours,
            "licenses": self.licenses,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Specialists:
        obj = Specialists(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            specialization=dto_dict.get("specialization"),
            working_hours=dto_dict.get("working_hours"),
            licenses=dto_dict.get("licenses"),
        )
        return obj
