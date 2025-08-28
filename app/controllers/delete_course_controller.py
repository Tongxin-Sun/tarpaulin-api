from ..helpers.verify_jwt import verify_jwt
from ..helpers.find_entity_by_id import find_entity_by_id
from ..helpers.find_entity_by_property import find_entity_by_property
from ..constants import COURSES, USERS, ENROLLMENT, ERROR_MESSAGE_403
from google.cloud import datastore

client = datastore.Client()


def delete_course_controller(request, course_id):
    payload = verify_jwt(request)

    if not find_entity_by_id(COURSES, course_id):
        return ERROR_MESSAGE_403, 403

    user = find_entity_by_property(USERS, "sub", payload["sub"], True)
    user_is_admin = user["role"] == "admin"
    if not user_is_admin:
        return ERROR_MESSAGE_403, 403

    course_key = client.key(COURSES, course_id)
    client.delete(course_key)
    query = client.query(kind=ENROLLMENT)
    query.add_filter("course_id", "=", course_id)
    enrollments = list(query.fetch())
    for e in enrollments:
        client.delete(e.key)
    return ("", 204)
