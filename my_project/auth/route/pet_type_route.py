from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import pet_type_controller
from my_project.auth.domain import PetType

pet_type_bp = Blueprint('pet_type', __name__, url_prefix='/pet_type')


@pet_type_bp.get('')
def get_all_pet_types() -> Response:
    return make_response(jsonify(pet_type_controller.find_all()), HTTPStatus.OK)


@pet_type_bp.get('/<int:pet_type_id>')
def get_pet_type(pet_type_id: int) -> Response:
    return make_response(jsonify(pet_type_controller.find_by_id(pet_type_id)), HTTPStatus.OK)


@pet_type_bp.post('')
def create_pet_type() -> Response:
    content = request.get_json()
    obj = PetType.create_from_dto(content)
    pet_type_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@pet_type_bp.put('/<int:pet_type_id>')
def update_pet_type(pet_type_id: int) -> Response:
    content = request.get_json()
    obj = PetType.create_from_dto(content)
    pet_type_controller.update(pet_type_id, obj)
    return make_response("Pet type updated", HTTPStatus.OK)


@pet_type_bp.patch('/<int:pet_type_id>')
def patch_pet_type(pet_type_id: int) -> Response:
    content = request.get_json()
    pet_type_controller.patch(pet_type_id, content)
    return make_response("Pet type updated", HTTPStatus.OK)


@pet_type_bp.delete('/<int:pet_type_id>')
def delete_pet_type(pet_type_id: int) -> Response:
    pet_type_controller.delete(pet_type_id)
    return make_response("Pet type deleted", HTTPStatus.OK)


@pet_type_bp.delete('/<int:status_id>')
def delete_report(status_id: int) -> Response:
    pet_type_controller.delete(status_id)
    return make_response("Report deleted", HTTPStatus.OK)
