from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto

client_pet = db.Table(
    "client_pet",
    db.Column("client_Id", db.Integer, db.ForeignKey("client.id")),
    db.Column("pet_id", db.Integer, db.ForeignKey("pet.id")),
    extend_existing=True
)
pet_diagnoses = db.Table(
    "pet_diagnoses",
    db.Column("diagnoses_id", db.Integer, db.ForeignKey("diagnoses.id")),
    db.Column("pet_id", db.Integer, db.ForeignKey("pet.id")),
    extend_existing=True
)


class Pet(db.Model, IDto):
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    breed = db.Column(db.String(45), nullable=True)
    last_visit_date = db.Column(db.String(45), nullable=True)
    medical_history = db.Column(db.String(300), nullable=True)
    photo = db.Column(db.BLOB, nullable=True)

    # ForeignKey
    pet_type_id = db.Column(db.Integer, db.ForeignKey('pet_type.id'), nullable=False)

    # Relationship 1:M
    pet_type = db.relationship("PetType", backref="pet_")

    # Relationship M:M
    clients = db.relationship('Client', secondary=client_pet,
                              backref=db.backref('pets_association_', lazy='dynamic'))
    diagnoses = db.relationship('Diagnoses', secondary=pet_diagnoses,
                                backref=db.backref('diagnoses_association_', lazy='dynamic'))
    scheduled_visit = db.relationship('ScheduledVisit', back_populates='pet')

    def __repr__(self) -> str:
        return f"Pet({self.id}, '{self.name}', '{self.age}', '{self.breed}', '{self.last_visit_date}'," \
               f" '{self.medical_history}', '{self.photo}', '{self.pet_type_id}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "breed": self.breed,
            "last_visit_date": self.last_visit_date,
            "medical_history": self.medical_history,
            "photo": self.photo,
            "pet_type_id": self.pet_type_id,

        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Pet:
        obj = Pet(
            name=dto_dict.get("name"),
            age=dto_dict.get("age"),
            breed=dto_dict.get("breed"),
            last_visit_date=dto_dict.get("last_visit_date"),
            medical_history=dto_dict.get("medical_history"),
            photo=dto_dict.get("photo"),
            pet_type_id=dto_dict.get("pet_type_id")
        )
        return obj
