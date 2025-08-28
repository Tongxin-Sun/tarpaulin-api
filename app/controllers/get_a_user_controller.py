from ..helpers.verify_jwt import verify_jwt
from ..helpers.find_entity_by_property import find_entity_by_property
from ..constants import USERS, COURSES, ENROLLMENT, PHOTO_BUCKET, ERROR_MESSAGE_403
from ..helpers.find_entity_by_id import find_entity_by_id
from ..helpers.error import AuthError
from google.cloud import storage


def get_a_user_controller(request, user_id):
    sub = verify_jwt(request)["sub"]
    auth_user = find_entity_by_property(USERS, "sub", sub, True)

    user = find_entity_by_id(USERS, user_id)

    if not user:
        raise AuthError(ERROR_MESSAGE_403, 403)

    if auth_user["role"] != "admin" and user["sub"] != sub:
        raise AuthError(ERROR_MESSAGE_403, 403)

    user["id"] = user.key.id

    if user["role"] == "instructor":
        courses = find_entity_by_property(COURSES, "instructor_id", user_id)
        user["courses"] = [
            f"{request.url_root}{COURSES}/{course.key.id}" for course in courses
        ]

    if user["role"] == "student":
        enrollments = find_entity_by_property(ENROLLMENT, "student_id", user_id)
        user["courses"] = [
            f"{request.url_root}{COURSES}/{e.get("course_id")}" for e in enrollments
        ]

    storage_client = storage.Client()
    bucket = storage_client.bucket(PHOTO_BUCKET)
    blob = bucket.blob(f"{user_id}.png")
    if blob.exists():
        user["avatar_url"] = f"{request.base_url}/avatar"
    return user, 200
