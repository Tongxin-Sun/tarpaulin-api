from flask import Blueprint, request
from ..constants import COURSES
from flasgger import swag_from
from ..controllers.update_course_controller import update_course_controller

update_course_bp = Blueprint("update_course_bp", __name__)


# Update a course by ID endpoint
@update_course_bp.route(f"/{COURSES}/<int:course_id>", methods=["PATCH"])
@swag_from("../../api/update_course.yml")
def update_course(course_id):
    return update_course_controller(request, course_id)
