from google.cloud import datastore
from ..constants import COURSES, ERROR_MESSAGE_404

client = datastore.Client()


def get_course_controller(request, course_id):
    course = client.get(client.key(COURSES, course_id))
    if course is None:
        return ERROR_MESSAGE_404, 404
    course["id"] = course.key.id
    course["self"] = request.base_url
    return course, 200
