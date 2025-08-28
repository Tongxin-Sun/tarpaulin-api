from ..helpers.verify_jwt import verify_jwt
from google.cloud import datastore
from ..constants import COURSES, ERROR_MESSAGE_403, ERROR_MESSAGE_400

client = datastore.Client()


def update_course_controller(request, course_id):
    # Check if the JWT is missing or invalid
    payload = verify_jwt(request)

    # Check if the JWT is valid, but the course doesn't exist.
    course = client.get(client.key(COURSES, course_id))
    if not course:
        return ERROR_MESSAGE_403, 403

    # Check if the JWT is valid, and the course exists, but the JWT doesn't belong to an admin.
    sub = payload["sub"]
    query = client.query(kind="users")
    query.add_filter("sub", "=", sub)
    user = list(query.fetch())[0]
    if not user["role"] == "admin":
        return ERROR_MESSAGE_403, 403

    content = request.get_json()
    if content.get("instructor_id") is not None:
        # Check if the instructor_id belongs to an instructor
        instructor = client.get(client.key("users", content["instructor_id"]))
        if not instructor or instructor["role"] != "instructor":
            return ERROR_MESSAGE_400, 400

    properties = ["subject", "number", "title", "term", "instructor_id"]
    for property in properties:
        if property in content:
            course[property] = content[property]

    client.put(course)
    course["id"] = course.key.id
    course["self"] = request.base_url
    return course, 200
