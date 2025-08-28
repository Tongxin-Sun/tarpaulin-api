from ..helpers.verify_jwt import verify_jwt
from ..helpers.find_entity_by_property import find_entity_by_property
from ..helpers.error import AuthError
from ..constants import USERS, ERROR_MESSAGE_403
from google.cloud import datastore

client = datastore.Client()


def get_all_users_controller(request):
    # Verify JWT and extract user identity
    sub = verify_jwt(request)["sub"]

    # Look up the authenticated user
    auth_user = find_entity_by_property(USERS, "sub", sub, True)

    # Check authorization
    if auth_user.get("role") != "admin":
        raise AuthError(ERROR_MESSAGE_403, 403)

    # Query datastore for all users
    all_users = list(client.query(kind="users").fetch())

    # Return only the allowed properties
    response = [
        {"id": user.key.id, "role": user["role"], "sub": user["sub"]}
        for user in all_users
    ]

    return response, 200
