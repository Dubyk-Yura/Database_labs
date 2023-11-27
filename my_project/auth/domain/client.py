from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto

client_pet = db.Table(
    "client_pet",
    db.Column("client_Id", db.Integer, db.ForeignKey("client.id")),
    db.Column("pet_id", db.Integer, db.ForeignKey("pet.id")),
    extend_existing=True
)


class Client(db.Model, IDto):
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    contact_number = db.Column(db.String(13), nullable=False)
    address = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=True)
    additional_contact_info = db.Column(db.String(150), nullable=True)

    # Relationship M:M
    pets = db.relationship('Pet', secondary=client_pet, backref=db.backref('clients_association', lazy='dynamic'))
    scheduled_visit = db.relationship('ScheduledVisit', back_populates='client')

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.name}', '{self.surname}', '{self.contact_number}', '{self.address}'," \
               f" '{self.email}', '{self.additional_contact_info}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "contact_number": self.contact_number,
            "address": self.address,
            "email": self.email,
            "additional_contact_info": self.additional_contact_info,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Client:
        obj = Client(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            contact_number=dto_dict.get("contact_number"),
            address=dto_dict.get("address"),
            email=dto_dict.get("email"),
            additional_contact_info=dto_dict.get("additional_contact_info")
        )
        return obj
