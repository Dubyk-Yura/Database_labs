from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import procedures_controller
from my_project.auth.domain import Procedures

procedures_bp = Blueprint('procedures', __name__, url_prefix='/procedures')


@procedures_bp.get('/<string:procedure_name>/name')
def get_procedure_by_name(procedure_name: str) -> Response:
    return make_response(jsonify(procedures_controller.find_by_name(procedure_name)), HTTPStatus.OK)


@procedures_bp.get('')
def get_all_procedures() -> Response:
    return make_response(jsonify(procedures_controller.find_all()), HTTPStatus.OK)


@procedures_bp.get('/<int:procedure_id>')
def get_procedure(procedure_id: int) -> Response:
    return make_response(jsonify(procedures_controller.find_by_id(procedure_id)), HTTPStatus.OK)


@procedures_bp.post('')
def create_procedure() -> Response:
    content = request.get_json()
    obj = Procedures.create_from_dto(content)
    procedures_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@procedures_bp.put('/<int:procedure_id>')
def update_procedure(procedure_id: int) -> Response:
    content = request.get_json()
    obj = Procedures.create_from_dto(content)
    procedures_controller.update(procedure_id, obj)
    return make_response("Procedure updated", HTTPStatus.OK)


@procedures_bp.patch('/<int:procedure_id>')
def patch_procedure(procedure_id: int) -> Response:
    content = request.get_json()
    procedures_controller.patch(procedure_id, content)
    return make_response("Procedure updated", HTTPStatus.OK)


@procedures_bp.delete('/<int:procedure_id>')
def delete_procedure(procedure_id: int) -> Response:
    procedures_controller.delete(procedure_id)
    return make_response("Procedure deleted", HTTPStatus.OK)
