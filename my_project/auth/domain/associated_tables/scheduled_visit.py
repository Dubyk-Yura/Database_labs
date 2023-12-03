from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class ScheduledVisit(db.Model, IDto):
    __tablename__ = "scheduled_visit"

    # Relationship M:M
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), primary_key=True, nullable=False)
    services_id = db.Column(db.Integer, db.ForeignKey('services.id'), primary_key=True, nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), primary_key=True, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), primary_key=True, nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), primary_key=True, nullable=False)

    status = db.relationship("Status", back_populates='scheduled_visit')
    report = db.relationship("Report", back_populates='scheduled_visit')
    client = db.relationship("Client", back_populates='scheduled_visit')
    services = db.relationship("Services", back_populates='scheduled_visit')
    pet = db.relationship("Pet", back_populates='scheduled_visit')

    def __repr__(self) -> str:
        return f"ScheduledVisit({self.client_id}, '{self.services_id}', '{self.pet_id}', '{self.status_id}', " \
               f"'{self.report_id}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "client_id": self.client_id,
            "services_id": self.services_id,
            "pet_id": self.pet_id,
            "status_id": self.status_id,
            "report_id": self.report_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> ScheduledVisit:
        obj = ScheduledVisit(
            client_id=dto_dict.get("client_id"),
            services_id=dto_dict.get("services_id"),
            pet_id=dto_dict.get("pet_id"),
            status_id=dto_dict.get("status_id"),
            report_id=dto_dict.get("report_id"),
        )
        return obj
