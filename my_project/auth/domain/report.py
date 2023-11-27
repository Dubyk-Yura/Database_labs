from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Report(db.Model, IDto):
    __tablename__ = "report"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    type = db.Column(db.String(45), nullable=False)
    date = db.Column(db.Date, nullable=False)
    link = db.Column(db.String(60), nullable=False, unique=True)

    # Relationship M:M
    scheduled_visit = db.relationship('ScheduledVisit', back_populates='report')

    def __repr__(self) -> str:
        return f"Report({self.id}, '{self.type}', '{self.date}', '{self.link}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "type": self.status,
            "date": self.type,
            "link": self.link,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Report:
        obj = Report(
            type=dto_dict.get("type"),
            date=dto_dict.get("date"),
            link=dto_dict.get("link")
        )
        return obj
