from ..helpers.verify_jwt import verify_jwt
from ..helpers.find_entity_by_property import find_entity_by_property
from ..helpers.require_course_access import require_course_access
from google.cloud import datastore
from ..constants import USERS

client = datastore.Client()


def get_enrollments_controller(request, course_id):
    enrolled_students = []

    # Check 401 error
    sub = verify_jwt(request)["sub"]

    # Check 403 error
    user = find_entity_by_property(USERS, "sub", sub, True)
    require_course_access(course_id, user)

    query = client.query(kind="enrollment")
    query.add_filter("course_id", "=", course_id)
    enrollments = list(query.fetch())

    for enrollment in enrollments:
        enrolled_students.append(enrollment["student_id"])

    return enrolled_students, 200
