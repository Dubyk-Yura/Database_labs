from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import client_controller
from my_project.auth.domain import Client

client_bp = Blueprint('client', __name__, url_prefix='/client')


@client_bp.get('/<int:client_id>/pets')
def get_client_by_pet(client_id: int) -> Response:
    return make_response(jsonify(client_controller.get_pets_for_client(client_id)), HTTPStatus.OK)


@client_bp.get('/<int:client_id>/services')
def get_client_by_services(client_id: int) -> Response:
    return make_response(jsonify(client_controller.get_services_for_client(client_id)), HTTPStatus.OK)


@client_bp.get('/<int:client_id>')
def get_client(client_id: int) -> Response:
    return make_response(jsonify(client_controller.find_by_id(client_id)), HTTPStatus.OK)


@client_bp.get('')
def get_all_clients() -> Response:
    return make_response(jsonify(client_controller.find_all()), HTTPStatus.OK)


@client_bp.post('/<int:client_id>/add_pet')
def connect_pet_and_client_from_client(client_id: int):
    try:
        data = request.get_json()
        pet_id = data.get('pet_id')
        client_controller.connect_pet_and_client_from_client(client_id, pet_id)
        return make_response(jsonify({"message": "Pet added successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@client_bp.post('')
def create_client() -> Response:
    content = request.get_json()
    obj = Client.create_from_dto(content)
    client_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@client_bp.put('/<int:client_id>')
def update_client(client_id: int) -> Response:
    content = request.get_json()
    obj = Client.create_from_dto(content)
    client_controller.update(client_id, obj)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.patch('/<int:client_id>')
def patch_client(client_id: int) -> Response:
    content = request.get_json()
    client_controller.patch(client_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.delete('/<int:client_id>')
def delete_client(client_id: int) -> Response:
    client_controller.delete(client_id)
    return make_response("Client deleted", HTTPStatus.OK)
