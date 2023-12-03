from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto

pet_diagnoses = db.Table(
    "pet_diagnoses",
    db.Column("diagnoses_id", db.Integer, db.ForeignKey("diagnoses.id")),
    db.Column("pet_id", db.Integer, db.ForeignKey("pet.id")),
    extend_existing=True
)


class Diagnoses(db.Model, IDto):
    __tablename__ = "diagnoses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    related_images = db.Column(db.BLOB, nullable=True)

    # Relationship 1:M
    treatment = db.relationship("Treatment", backref="diagnoses_")

    # Relationship M:M
    pets = db.relationship('Pet', secondary=pet_diagnoses,
                           backref=db.backref('pets_association_', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Diagnoses({self.id}, '{self.name}', '{self.description}', '{self.related_images}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "related_images": self.related_images,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Diagnoses:
        obj = Diagnoses(
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            related_images=dto_dict.get("related_images"),
        )
        return obj
