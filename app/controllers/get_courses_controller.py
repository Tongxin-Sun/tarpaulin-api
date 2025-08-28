from google.cloud import datastore

client = datastore.Client()


# Get all courses endpoint
def get_courses_controller(request):
    courses_response = []
    limit = request.args.get("limit", default=3, type=int)
    offset = request.args.get("offset", default=0, type=int)
    query = client.query(kind="courses")
    query.order = ["subject"]
    courses_iterator = query.fetch(limit=limit, offset=offset)
    pages = courses_iterator.pages
    courses = list(next(pages))
    for course in courses:
        course["id"] = course.key.id
        course["self"] = f"{request.base_url}/{course.key.id}"
        courses_response.append(course)

    response = {"courses": courses_response}

    if courses_iterator.next_page_token:
        response["next"] = f"{request.base_url}?limit={limit}&offset={offset + limit}"

    return response, 200
