from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import diagnoses_controller
from my_project.auth.domain import Diagnoses

diagnoses_bp = Blueprint('diagnoses', __name__, url_prefix='/diagnoses')


@diagnoses_bp.get('/<int:diagnoses_id>/pets')
def get_pets_for_diagnoses(diagnoses_id: int) -> Response:
    return make_response(jsonify(diagnoses_controller.get_pets_for_diagnoses(diagnoses_id)), HTTPStatus.OK)


@diagnoses_bp.get('')
def get_all_diagnoses() -> Response:
    return make_response(jsonify(diagnoses_controller.find_all()), HTTPStatus.OK)


@diagnoses_bp.get('/<int:diagnoses_id>')
def get_diagnoses(diagnoses_id: int) -> Response:
    return make_response(jsonify(diagnoses_controller.find_by_id(diagnoses_id)), HTTPStatus.OK)


@diagnoses_bp.post('/<int:diagnoses_id>/add_pet')
def connect_pet_and_diagnoses_from_pet(diagnoses_id: int):
    try:
        data = request.get_json()
        pet_id = data.get('pet_id')
        diagnoses_controller.connect_pet_and_diagnoses_from_diagnoses(diagnoses_id, pet_id)
        return make_response(jsonify({"message": "Diagnoses added successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


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


@diagnoses_bp.patch('/<int:diagnoses_id>/remove_pet')
def remove_pet_from_client(diagnoses_id) -> Response:
    try:
        data = request.get_json()
        pet_id = data.get('pet_id')
        diagnoses_controller.remove_pet_from_diagnoses(diagnoses_id, pet_id)
        return make_response(jsonify({"message": "Pet removed successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@diagnoses_bp.delete('/<int:diagnoses_id>')
def delete_diagnoses(diagnoses_id: int) -> Response:
    diagnoses_controller.delete(diagnoses_id)
    return make_response("Diagnoses deleted", HTTPStatus.OK)
