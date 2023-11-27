from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import treatment_medicine_controller
from my_project.auth.domain import TreatmentMedicine

treatment_medicine_bp = Blueprint('treatment_medicine', __name__, url_prefix='/treatment_medicine')


@treatment_medicine_bp.get('')
def get_all_treatment_medicines() -> Response:
    return make_response(jsonify(treatment_medicine_controller.find_all()), HTTPStatus.OK)


@treatment_medicine_bp.get('/<int:treatment_medicine_id>')
def get_treatment_medicine(treatment_medicine_id: int) -> Response:
    return make_response(jsonify(treatment_medicine_controller.find_by_id(treatment_medicine_id)), HTTPStatus.OK)


@treatment_medicine_bp.post('')
def create_treatment_medicine() -> Response:
    content = request.get_json()
    obj = TreatmentMedicine.create_from_dto(content)
    treatment_medicine_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@treatment_medicine_bp.put('/<int:treatment_medicine_id>')
def update_treatment_medicine(treatment_medicine_id: int) -> Response:
    content = request.get_json()
    obj = TreatmentMedicine.create_from_dto(content)
    treatment_medicine_controller.update(treatment_medicine_id, obj)
    return make_response("Treatment medicine updated", HTTPStatus.OK)


@treatment_medicine_bp.patch('/<int:treatment_medicine_id>')
def patch_treatment_medicine(treatment_medicine_id: int) -> Response:
    content = request.get_json()
    treatment_medicine_controller.patch(treatment_medicine_id, content)
    return make_response("Treatment medicine updated", HTTPStatus.OK)


@treatment_medicine_bp.delete('/<int:treatment_medicine_id>')
def delete_treatment_medicine(treatment_medicine_id: int) -> Response:
    treatment_medicine_controller.delete(treatment_medicine_id)
    return make_response("Treatment medicine deleted", HTTPStatus.OK)
