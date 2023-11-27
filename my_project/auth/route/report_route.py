from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import report_controller
from my_project.auth.domain import Report

report_bp = Blueprint('report', __name__, url_prefix='/report')


@report_bp.get('')
def get_all_report() -> Response:
    return make_response(jsonify(report_controller.find_all()), HTTPStatus.OK)


@report_bp.get('/<int:report_id>')
def get_report(report_id: int) -> Response:
    return make_response(jsonify(report_controller.find_by_id(report_id)), HTTPStatus.OK)


@report_bp.post('')
def create_report() -> Response:
    content = request.get_json()
    obj = Report.create_from_dto(content)
    report_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@report_bp.put('/<int:report_id>')
def update_report(report_id: int) -> Response:
    content = request.get_json()
    obj = Report.create_from_dto(content)
    report_controller.update(report_id, obj)
    return make_response("Report updated", HTTPStatus.OK)


@report_bp.patch('/<int:report_id>')
def patch_report(report_id: int) -> Response:
    content = request.get_json()
    report_controller.patch(report_id, content)
    return make_response("Report updated", HTTPStatus.OK)


@report_bp.delete('/<int:status_id>')
def delete_report(status_id: int) -> Response:
    report_controller.delete(status_id)
    return make_response("Report deleted", HTTPStatus.OK)
