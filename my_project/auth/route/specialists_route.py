from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import specialists_controller
from my_project.auth.domain import Specialists

specialists_bp = Blueprint('specialists', __name__, url_prefix='/specialists')


@specialists_bp.get('/<string:specialist_name>/name')
def get_specialist_by_name(specialist_name: str) -> Response:
    return make_response(jsonify(specialists_controller.find_by_name(specialist_name)), HTTPStatus.OK)


@specialists_bp.get('')
def get_all_specialists() -> Response:
    return make_response(jsonify(specialists_controller.find_all()), HTTPStatus.OK)


@specialists_bp.get('/<int:specialist_id>')
def get_specialist(specialist_id: int) -> Response:
    return make_response(jsonify(specialists_controller.find_by_id(specialist_id)), HTTPStatus.OK)


@specialists_bp.post('')
def create_specialist() -> Response:
    content = request.get_json()
    obj = Specialists.create_from_dto(content)
    specialists_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@specialists_bp.put('/<int:specialist_id>')
def update_specialist(specialist_id: int) -> Response:
    content = request.get_json()
    obj = Specialists.create_from_dto(content)
    specialists_controller.update(specialist_id, obj)
    return make_response("Specialist updated", HTTPStatus.OK)


@specialists_bp.patch('/<int:specialist_id>')
def patch_specialist(specialist_id: int) -> Response:
    content = request.get_json()
    specialists_controller.patch(specialist_id, content)
    return make_response("Specialist updated", HTTPStatus.OK)


@specialists_bp.delete('/<int:specialist_id>')
def delete_specialist(specialist_id: int) -> Response:
    specialists_controller.delete(specialist_id)
    return make_response("Specialist deleted", HTTPStatus.OK)
