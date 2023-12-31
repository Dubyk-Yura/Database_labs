from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import status_controller
from my_project.auth.domain import Status

status_bp = Blueprint('status', __name__, url_prefix='/status')


@status_bp.get('')
def get_all_status() -> Response:
    """
    Gets all status objects.
    :return: Response object
    """
    return make_response(jsonify(status_controller.find_all()), HTTPStatus.OK)


@status_bp.get('/<int:status_id>')
def get_status(status_id: int) -> Response:
    """
    Gets status by ID.
    :return: Response object
    """
    return make_response(jsonify(status_controller.find_by_id(status_id)), HTTPStatus.OK)


@status_bp.post('/convert_rows_in_databases')
def convert_rows_in_databases() -> Response:
    try:
        status_controller.convert_rows_in_databases()
        return make_response(jsonify({"message": "databases creates successfully"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@status_bp.post('')
def create_status() -> Response:
    """
    Creates a new status object.
    :return: Response object
    """
    content = request.get_json()
    status = Status.create_from_dto(content)
    status_controller.create(status)
    return make_response(jsonify(status.put_into_dto()), HTTPStatus.CREATED)


@status_bp.put('/<int:status_id>')
def update_status(status_id: int) -> Response:
    """
    Updates status by ID.
    :return: Response object
    """
    content = request.get_json()
    status = Status.create_from_dto(content)
    status_controller.update(status_id, status)
    return make_response("Status updated", HTTPStatus.OK)


@status_bp.patch('/<int:status_id>')
def patch_status(status_id: int) -> Response:
    """
    Patches status by ID.
    :return: Response object
    """
    content = request.get_json()
    status_controller.patch(status_id, content)
    return make_response("Status updated", HTTPStatus.OK)


@status_bp.delete('/<int:status_id>')
def delete_status(status_id: int) -> Response:
    """
    Deletes status by ID.
    :return: Response object
    """
    status_controller.delete(status_id)
    return make_response("Status deleted", HTTPStatus.OK)
