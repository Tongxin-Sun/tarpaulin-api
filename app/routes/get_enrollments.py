from flask import Blueprint, request
from ..constants import COURSES
from flasgger import swag_from
from ..controllers.get_enrollments_controller import get_enrollments_controller

get_enrollments_bp = Blueprint("get_enrollments_bp", __name__)


@get_enrollments_bp.route(f"/{COURSES}/<int:course_id>/students")
@swag_from("../../api/get_enrollments.yml")
def get_enrollments(course_id):
    return get_enrollments_controller(request, course_id)
