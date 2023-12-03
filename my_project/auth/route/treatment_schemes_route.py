from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import treatment_schemes_controller
from my_project.auth.domain import TreatmentSchemes

treatment_schemes_bp = Blueprint('treatment_schemes', __name__, url_prefix='/treatment_schemes')


@treatment_schemes_bp.get('')
def get_all_treatment_schemes() -> Response:
    return make_response(jsonify(treatment_schemes_controller.find_all()), HTTPStatus.OK)


@treatment_schemes_bp.get('/<int:treatment_scheme_id>')
def get_treatment_scheme(treatment_scheme_id: int) -> Response:
    return make_response(jsonify(treatment_schemes_controller.find_by_id(treatment_scheme_id)), HTTPStatus.OK)


@treatment_schemes_bp.post('')
def create_treatment_scheme() -> Response:
    content = request.get_json()
    obj = TreatmentSchemes.create_from_dto(content)
    treatment_schemes_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@treatment_schemes_bp.put('/<int:treatment_scheme_id>')
def update_treatment_scheme(treatment_scheme_id: int) -> Response:
    content = request.get_json()
    obj = TreatmentSchemes.create_from_dto(content)
    treatment_schemes_controller.update(treatment_scheme_id, obj)
    return make_response("Treatment Scheme updated", HTTPStatus.OK)


@treatment_schemes_bp.patch('/<int:treatment_scheme_id>')
def patch_treatment_scheme(treatment_scheme_id: int) -> Response:
    content = request.get_json()
    treatment_schemes_controller.patch(treatment_scheme_id, content)
    return make_response("Treatment Scheme updated", HTTPStatus.OK)


@treatment_schemes_bp.delete('/<int:treatment_scheme_id>')
def delete_treatment_scheme(treatment_scheme_id: int) -> Response:
    treatment_schemes_controller.delete(treatment_scheme_id)
    return make_response("Treatment Scheme deleted", HTTPStatus.OK)