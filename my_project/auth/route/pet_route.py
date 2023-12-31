from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import pet_controller
from my_project.auth.domain import Pet

pet_bp = Blueprint('pet', __name__, url_prefix='/pet')


@pet_bp.get('/<int:pet_id>/clients')
def get_clients_for_pet(pet_id: int) -> Response:
    return make_response(jsonify(pet_controller.get_clients_for_pet(pet_id)), HTTPStatus.OK)


@pet_bp.get('/<int:pet_id>/diagnoses')
def get_diagnoses_for_pet(pet_id: int) -> Response:
    return make_response(jsonify(pet_controller.get_diagnoses_for_pet(pet_id)), HTTPStatus.OK)


@pet_bp.get('')
def get_all_pets() -> Response:
    return make_response(jsonify(pet_controller.find_all()), HTTPStatus.OK)


@pet_bp.get('/<int:pet_id>')
def get_pet(pet_id: int) -> Response:
    return make_response(jsonify(pet_controller.find_by_id(pet_id)), HTTPStatus.OK)


@pet_bp.post('/<int:pet_id>/add_client')
def connect_pet_and_client_from_pet(pet_id: int):
    try:
        data = request.get_json()
        client_id = data.get('client_id')

        pet_controller.connect_pet_and_client_from_pet(pet_id, client_id)

        return make_response(jsonify({"message": "Pet added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@pet_bp.post('/<int:pet_id>/add_diagnoses')
def connect_pet_and_diagnoses_from_pet(pet_id: int):
    try:
        data = request.get_json()
        diagnoses_id = data.get('diagnoses_id')
        pet_controller.connect_pet_and_diagnoses_from_pet(pet_id, diagnoses_id)
        return make_response(jsonify({"message": "Diagnoses added successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@pet_bp.post('')
def create_pet() -> Response:
    content = request.get_json()
    obj = Pet.create_from_dto(content)
    pet_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@pet_bp.post('/add_client_pet')
def insert_in_client_pet_by_values() -> Response:
    content = request.get_json()
    client_name = content.get('client_name')
    client_surname = content.get('client_surname')
    client_contact_number = content.get('client_contact_number')
    pet_name = content.get('pet_name')
    pet_age = content.get('pet_age')
    if any(arg is None for arg in [client_name, client_surname, client_contact_number, pet_name, pet_age]):
        return make_response(jsonify({"error": "Missing required fields"}), HTTPStatus.BAD_REQUEST)
    try:
        pet_controller.insert_in_client_pet_by_values(client_name, client_surname, client_contact_number, pet_name,
                                                      pet_age)
        return make_response(jsonify({"message": "successful connecting"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@pet_bp.put('/<int:pet_id>')
def update_pet(pet_id: int) -> Response:
    content = request.get_json()
    obj = Pet.create_from_dto(content)
    pet_controller.update(pet_id, obj)
    return make_response("Pet updated", HTTPStatus.OK)


@pet_bp.patch('/<int:pet_id>')
def patch_pet(pet_id: int) -> Response:
    content = request.get_json()
    pet_controller.patch(pet_id, content)
    return make_response("Pet updated", HTTPStatus.OK)


@pet_bp.patch('/<int:pet_id>/remove_client')
def remove_client_from_pet(pet_id) -> Response:
    try:
        data = request.get_json()
        client_id = data.get('client_id')
        pet_controller.remove_client_from_pet(pet_id, client_id)
        return make_response(jsonify({"message": "Client removed successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@pet_bp.patch('/<int:pet_id>/remove_diagnoses')
def remove_diagnoses_from_pet(pet_id) -> Response:
    try:
        data = request.get_json()
        diagnoses_id = data.get('diagnoses_id')
        pet_controller.remove_diagnoses_from_pet(pet_id, diagnoses_id)
        return make_response(jsonify({"message": "Diagnoses removed successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@pet_bp.delete('/<int:pet_id>')
def delete_pet(pet_id: int) -> Response:
    pet_controller.delete(pet_id)
    return make_response("Pet deleted", HTTPStatus.OK)
