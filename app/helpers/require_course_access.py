from ..helpers.find_entity_by_id import find_entity_by_id
from ..constants import COURSES, ERROR_MESSAGE_403
from ..helpers.error import AuthError


def require_course_access(course_id, user):
    course = find_entity_by_id(COURSES, course_id)
    if not course or (
        user["role"] != "admin" and course["instructor_id"] != user.key.id
    ):
        raise AuthError(ERROR_MESSAGE_403, 403)
