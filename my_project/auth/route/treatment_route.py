from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import treatment_controller
from my_project.auth.domain import Treatment

treatment_bp = Blueprint('treatment', __name__, url_prefix='/treatment')


@treatment_bp.get('/<int:treatment_id>')
def get_treatment(treatment_id: int) -> Response:
    return make_response(jsonify(treatment_controller.find_by_id(treatment_id)), HTTPStatus.OK)


@treatment_bp.get('')
def get_all_treatments() -> Response:
    return make_response(jsonify(treatment_controller.find_all()), HTTPStatus.OK)


@treatment_bp.post('')
def create_treatment() -> Response:
    content = request.get_json()
    obj = Treatment.create_from_dto(content)
    treatment_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@treatment_bp.put('/<int:treatment_id>')
def update_treatment(treatment_id: int) -> Response:
    content = request.get_json()
    obj = Treatment.create_from_dto(content)
    treatment_controller.update(treatment_id, obj)
    return make_response("Treatment updated", HTTPStatus.OK)


@treatment_bp.patch('/<int:treatment_id>')
def patch_treatment(treatment_id: int) -> Response:
    content = request.get_json()
    treatment_controller.patch(treatment_id, content)
    return make_response("Treatment updated", HTTPStatus.OK)


@treatment_bp.delete('/<int:treatment_id>')
def delete_treatment(treatment_id: int) -> Response:
    treatment_controller.delete(treatment_id)
    return make_response("Treatment deleted", HTTPStatus.OK)