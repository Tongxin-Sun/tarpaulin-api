from ..helpers.verify_jwt import verify_jwt
from ..helpers.find_entity_by_property import find_entity_by_property
from ..helpers.find_entity_by_id import find_entity_by_id
from ..constants import USERS, ERROR_MESSAGE_409
from google.cloud import datastore
from ..helpers.require_course_access import require_course_access

client = datastore.Client()


def update_enrollment_controller(request, course_id):
    # Check 401 error
    sub = verify_jwt(request)["sub"]

    # Check 403 error
    user = find_entity_by_property(USERS, "sub", sub, True)
    require_course_access(course_id, user)

    added_students = request.get_json().get("add")
    removed_students = request.get_json().get("remove")
    common_students = set(added_students) & set(removed_students)
    if common_students:
        return ERROR_MESSAGE_409, 409

    for student_id in added_students:
        user = find_entity_by_id(USERS, student_id)
        if not user or user["role"] != "student":
            return ERROR_MESSAGE_409, 409
        query = client.query(kind="enrollment")
        query.add_filter("course_id", "=", course_id)
        query.add_filter("student_id", "=", student_id)
        results = list(query.fetch())

        if not results:
            enrollment = datastore.Entity(client.key("enrollment"))
            enrollment.update({"course_id": course_id, "student_id": student_id})
            client.put(enrollment)

    for student_id in removed_students:
        user = find_entity_by_id(USERS, student_id)
        if not user or user["role"] != "student":
            return ERROR_MESSAGE_409, 409
        query = client.query(kind="enrollment")
        query.add_filter("course_id", "=", course_id)
        query.add_filter("student_id", "=", student_id)
        results = list(query.fetch())

        if results:
            enrollment_entity = results[0]
            client.delete(enrollment_entity.key)

    return "", 200
