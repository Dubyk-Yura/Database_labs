from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Services(db.Model, IDto):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    description = db.Column(db.String(45), nullable=True)

    # ForeignKey
    specialists_id = db.Column(db.Integer, db.ForeignKey('specialists.id'), nullable=False)

    # Relationship 1:M
    specialists = db.relationship("Specialists", backref="services_")

    # Relationship M:M
    scheduled_visit = db.relationship('ScheduledVisit', back_populates='services')

    def __repr__(self) -> str:
        return f"Services({self.id}, '{self.name}', '{self.price}', '{self.duration}', '{self.description}'," \
               f" '{self.specialists_id}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "duration": self.duration,
            "description": self.description,
            "specialists_id": self.specialists_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Services:
        obj = Services(
            name=dto_dict.get("name"),
            price=dto_dict.get("price"),
            duration=dto_dict.get("duration"),
            description=dto_dict.get("description"),
            specialists_id=dto_dict.get("specialists_id")
        )
        return obj
