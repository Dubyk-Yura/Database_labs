from __future__ import annotations

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Medicine(db.Model, IDto):
    __tablename__ = "medicine"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    form = db.Column(db.String(45), nullable=False)
    dose = db.Column(db.String(45), nullable=True)

    # Relationship 1:M
    medicine_procedures_schemes = db.relationship("MedicineProceduresSchemes", backref="medicine_", uselist=False)

    def __repr__(self) -> str:
        return f"Medicine({self.id}, '{self.name}', '{self.price}', '{self.form}', '{self.dose}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "form": self.form,
            "dose": self.dose,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Medicine:
        obj = Medicine(
            name=dto_dict.get("name"),
            price=dto_dict.get("price"),
            form=dto_dict.get("form"),
            dose=dto_dict.get("dose"),
        )
        return obj
