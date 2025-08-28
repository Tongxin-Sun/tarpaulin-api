from flask import Blueprint, request
from ..constants import COURSES
from flasgger import swag_from
from ..controllers.get_course_controller import get_course_controller

get_course_bp = Blueprint("get_course_bp", __name__)


@get_course_bp.route(f"/{COURSES}/<int:course_id>")
@swag_from("../../api/get_course.yml")
def get_course(course_id):
    return get_course_controller(request, course_id)
