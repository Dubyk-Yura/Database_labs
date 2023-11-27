from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import diagnoses_controller
from my_project.auth.domain import Diagnoses

diagnoses_bp = Blueprint('diagnoses', __name__, url_prefix='/diagnoses')


@diagnoses_bp.get('/<int:diagnoses_id>/pets')
def get_pets_for_diagnoses(diagnoses_id: int) -> Response:
    return make_response(jsonify(diagnoses_controller.get_pets_for_diagnoses(diagnoses_id)), HTTPStatus.OK)


@diagnoses_bp.get('/<string:diagnoses_name>/name')
def get_diagnoses_by_name(diagnoses_name: str) -> Response:
    return make_response(jsonify(diagnoses_controller.find_by_name(diagnoses_name)), HTTPStatus.OK)


@diagnoses_bp.get('')
def get_all_diagnoses() -> Response:
    return make_response(jsonify(diagnoses_controller.find_all()), HTTPStatus.OK)


@diagnoses_bp.get('/<int:diagnoses_id>')
def get_diagnoses(diagnoses_id: int) -> Response:
    return make_response(jsonify(diagnoses_controller.find_by_id(diagnoses_id)), HTTPStatus.OK)


@diagnoses_bp.post('')
def create_diagnoses() -> Response:
    content = request.get_json()
    obj = Diagnoses.create_from_dto(content)
    diagnoses_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@diagnoses_bp.put('/<int:diagnoses_id>')
def update_diagnoses(diagnoses_id: int) -> Response:
    content = request.get_json()
    obj = Diagnoses.create_from_dto(content)
    diagnoses_controller.update(diagnoses_id, obj)
    return make_response("Diagnoses updated", HTTPStatus.OK)


@diagnoses_bp.patch('/<int:diagnoses_id>')
def patch_diagnoses(diagnoses_id: int) -> Response:
    content = request.get_json()
    diagnoses_controller.patch(diagnoses_id, content)
    return make_response("Diagnoses updated", HTTPStatus.OK)


@diagnoses_bp.delete('/<int:diagnoses_id>')
def delete_diagnoses(diagnoses_id: int) -> Response:
    diagnoses_controller.delete(diagnoses_id)
    return make_response("Diagnoses deleted", HTTPStatus.OK)
