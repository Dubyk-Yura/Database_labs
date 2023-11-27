from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Status(db.Model, IDto):
    __tablename__ = "status"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    status = db.Column(db.String(45), unique=True, nullable=False)

    # Relationship M:M
    scheduled_visit = db.relationship('ScheduledVisit', back_populates='status')

    def __repr__(self) -> str:
        return f"Status({self.id}, '{self.status}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "status": self.status,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Status:
        obj = Status(
            status=dto_dict.get("status")
        )
        return obj
