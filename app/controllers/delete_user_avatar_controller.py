from ..helpers.verify_jwt import verify_jwt
from google.cloud import datastore, storage
from ..constants import USERS, ERROR_MESSAGE_403, ERROR_MESSAGE_404, PHOTO_BUCKET
from ..helpers.error import AuthError

client = datastore.Client()


def delete_user_avatar_controller(request, user_id):
    # Check if the JWT is missing or invalid
    sub = verify_jwt(request)["sub"]

    user = client.get(client.key(USERS, user_id))
    if not user or user["sub"] != sub:
        raise AuthError(ERROR_MESSAGE_403, 403)

    file_name = f"{user_id}.png"
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(PHOTO_BUCKET)
    blob = bucket.blob(file_name)

    if not blob.exists():
        raise AuthError(ERROR_MESSAGE_404, 404)

    blob.delete()

    return "", 204
