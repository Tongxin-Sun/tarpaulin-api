from ..helpers.verify_jwt import verify_jwt
from google.cloud import datastore
from ..helpers.find_entity_by_property import find_entity_by_property
from ..constants import USERS, ERROR_MESSAGE_403, COURSES, ERROR_MESSAGE_400
from ..helpers.error import AuthError

client = datastore.Client()


def create_course_controller(request):
    sub = verify_jwt(request)["sub"]

    """query = client.query(kind="users")
    query.add_filter("sub", "=", sub)
    user = list(query.fetch())[0]"""
    user = find_entity_by_property(USERS, "sub", sub, one_result=True)

    if not user["role"] == "admin":
        raise AuthError(ERROR_MESSAGE_403, 403)

    content = request.get_json()
    new_course = datastore.Entity(client.key(COURSES))

    required_attributes = ["subject", "number", "title", "term", "instructor_id"]
    if not all(attribute in content for attribute in required_attributes):
        raise AuthError(ERROR_MESSAGE_400, 400)

    # Check if the instructor_id is valid
    instructor = client.get(client.key("users", content["instructor_id"]))
    if not instructor or instructor["role"] != "instructor":
        raise AuthError(ERROR_MESSAGE_400, 400)

    new_course.update(
        {
            "subject": content["subject"],
            "number": content["number"],
            "title": content["title"],
            "term": content["term"],
            "instructor_id": content["instructor_id"],
        }
    )

    client.put(new_course)
    new_course["id"] = new_course.key.id
    new_course["self"] = f"{request.base_url}/{new_course.key.id}"
    return new_course, 201
