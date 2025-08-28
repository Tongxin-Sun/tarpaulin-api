from flask import Blueprint, request
from ..constants import COURSES
from flasgger import swag_from
from ..controllers.update_enrollment_controller import update_enrollment_controller

update_enrollment_bp = Blueprint("update_enrollment_bp", __name__)


# Enroll and/or disenroll a student from a course endpoint
@update_enrollment_bp.route(f"/{COURSES}/<int:course_id>/students", methods=["PATCH"])
@swag_from("../../api/update_enrollment.yml")
def update_enrollment(course_id):
    return update_enrollment_controller(request, course_id)
