from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import services_controller
from my_project.auth.domain import Services

services_bp = Blueprint('services', __name__, url_prefix='/services')


@services_bp.get('/<int:service_id>/clients')
def get_services_by_clients(service_id: int) -> Response:
    return make_response(jsonify(services_controller.get_clients_for_service(service_id)), HTTPStatus.OK)


@services_bp.get('')
def get_all_services() -> Response:
    return make_response(jsonify(services_controller.find_all()), HTTPStatus.OK)


@services_bp.get('/<int:service_id>')
def get_service(service_id: int) -> Response:
    return make_response(jsonify(services_controller.find_by_id(service_id)), HTTPStatus.OK)


@services_bp.post('')
def create_service() -> Response:
    content = request.get_json()
    obj = Services.create_from_dto(content)
    services_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@services_bp.put('/<int:service_id>')
def update_service(service_id: int) -> Response:
    content = request.get_json()
    obj = Services.create_from_dto(content)
    services_controller.update(service_id, obj)
    return make_response("Service updated", HTTPStatus.OK)


@services_bp.patch('/<int:service_id>')
def patch_service(service_id: int) -> Response:
    content = request.get_json()
    services_controller.patch(service_id, content)
    return make_response("Service updated", HTTPStatus.OK)


@services_bp.delete('/<int:service_id>')
def delete_service(service_id: int) -> Response:
    services_controller.delete(service_id)
    return make_response("Service deleted", HTTPStatus.OK)
