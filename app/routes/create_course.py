from flask import Blueprint, request
from ..constants import COURSES
from ..controllers.create_course_controller import create_course_controller
from flasgger import swag_from

create_course_bp = Blueprint("create_course_bp", __name__)


@create_course_bp.route(f"/{COURSES}", methods=["POST"])
@swag_from("../../api/create_course.yml")
def create_course():
    return create_course_controller(request)
