from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import medicine_procedures_schemes_controller
from my_project.auth.domain import MedicineProceduresSchemes

medicine_procedures_schemes_bp = Blueprint('medicine_procedures_schemes', __name__,
                                           url_prefix='/medicine_procedures_schemes')


@medicine_procedures_schemes_bp.get('/<int:medicine_id>/medicine_id')
def get_by_medicine_id(medicine_id: int) -> Response:
    return make_response(jsonify(medicine_procedures_schemes_controller.find_by_medicine_id(medicine_id)),
                         HTTPStatus.OK)


@medicine_procedures_schemes_bp.get('')
def get_all_medicine_procedures_schemes() -> Response:
    return make_response(jsonify(medicine_procedures_schemes_controller.find_all()), HTTPStatus.OK)


@medicine_procedures_schemes_bp.get('/<int:medicine_procedures_scheme_id>')
def get_medicine_procedures_scheme(medicine_procedures_scheme_id: int) -> Response:
    return make_response(jsonify(medicine_procedures_schemes_controller.find_by_id(medicine_procedures_scheme_id)),
                         HTTPStatus.OK)


@medicine_procedures_schemes_bp.post('')
def create_medicine_procedures_scheme() -> Response:
    content = request.get_json()
    obj = MedicineProceduresSchemes.create_from_dto(content)
    medicine_procedures_schemes_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@medicine_procedures_schemes_bp.put('/<int:medicine_procedures_scheme_id>')
def update_medicine_procedures_scheme(medicine_procedures_scheme_id: int) -> Response:
    content = request.get_json()
    obj = MedicineProceduresSchemes.create_from_dto(content)
    medicine_procedures_schemes_controller.update(medicine_procedures_scheme_id, obj)
    return make_response("Medicine procedure scheme updated", HTTPStatus.OK)


@medicine_procedures_schemes_bp.patch('/<int:medicine_procedures_scheme_id>')
def patch_medicine_procedures_scheme(medicine_procedures_scheme_id: int) -> Response:
    content = request.get_json()
    medicine_procedures_schemes_controller.patch(medicine_procedures_scheme_id, content)
    return make_response("Medicine procedure scheme updated", HTTPStatus.OK)


@medicine_procedures_schemes_bp.delete('/<int:medicine_procedures_scheme_id>')
def delete_medicine_procedures_scheme(medicine_procedures_scheme_id: int) -> Response:
    medicine_procedures_schemes_controller.delete(medicine_procedures_scheme_id)
    return make_response("Medicine procedure scheme deleted", HTTPStatus.OK)
