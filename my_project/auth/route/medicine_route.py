from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import medicine_controller
from my_project.auth.domain import Medicine

medicine_bp = Blueprint('medicine', __name__, url_prefix='/medicine')


@medicine_bp.get('/<string:medicine_name>/name')
def get_medicine_by_name(medicine_name: str) -> Response:
    return make_response(jsonify(medicine_controller.find_by_name(medicine_name)), HTTPStatus.OK)


@medicine_bp.get('')
def get_all_medicines() -> Response:
    return make_response(jsonify(medicine_controller.find_all()), HTTPStatus.OK)


@medicine_bp.get('/<int:medicine_id>')
def get_medicine(medicine_id: int) -> Response:
    return make_response(jsonify(medicine_controller.find_by_id(medicine_id)), HTTPStatus.OK)


@medicine_bp.post('')
def create_medicine() -> Response:
    content = request.get_json()
    obj = Medicine.create_from_dto(content)
    medicine_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@medicine_bp.put('/<int:medicine_id>')
def update_medicine(medicine_id: int) -> Response:
    content = request.get_json()
    obj = Medicine.create_from_dto(content)
    medicine_controller.update(medicine_id, obj)
    return make_response("Medicine updated", HTTPStatus.OK)


@medicine_bp.patch('/<int:medicine_id>')
def patch_medicine(medicine_id: int) -> Response:
    content = request.get_json()
    medicine_controller.patch(medicine_id, content)
    return make_response("Medicine updated", HTTPStatus.OK)


@medicine_bp.delete('/<int:medicine_id>')
def delete_medicine(medicine_id: int) -> Response:
    medicine_controller.delete(medicine_id)
    return make_response("Medicine deleted", HTTPStatus.OK)
