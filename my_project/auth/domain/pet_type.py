from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class PetType(db.Model, IDto):
    __tablename__ = "pet_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    type = db.Column(db.String(45), nullable=False, unique=True)

    # Relationship 1:M
    pet = db.relationship("Pet", backref="pet_type_", uselist=False)

    def __repr__(self) -> str:
        return f"PetType({self.id}, '{self.type}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "type": self.type,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> PetType:
        obj = PetType(
            type=dto_dict.get("type"),
        )
        return obj
