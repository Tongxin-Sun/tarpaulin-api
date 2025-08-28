from flask import Blueprint, request
from ..constants import COURSES
from flasgger import swag_from
from ..controllers.get_courses_controller import get_courses_controller

get_courses_bp = Blueprint("get_courses_bp", __name__)


@get_courses_bp.route(f"/{COURSES}")
@swag_from("../../api/get_courses.yml")
def get_courses():
    return get_courses_controller(request)
