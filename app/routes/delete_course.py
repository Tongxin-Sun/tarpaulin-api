from flask import Blueprint, request
from ..constants import COURSES
from flasgger import swag_from
from ..controllers.delete_course_controller import delete_course_controller

delete_course_bp = Blueprint("delete_course_bp", __name__)


# Delete a course by ID endpoint
@delete_course_bp.route(f"/{COURSES}/<int:course_id>", methods=["DELETE"])
@swag_from("../../api/delete_course.yml")
def delete_course(course_id):
    return delete_course_controller(request, course_id)
