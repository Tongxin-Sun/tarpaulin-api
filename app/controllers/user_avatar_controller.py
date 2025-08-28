import io
from flask import send_file
from google.cloud import storage
from ..helpers.verify_jwt import verify_jwt
from ..helpers.error import AuthError
from ..constants import USERS, PHOTO_BUCKET, ERROR_MESSAGE_403, ERROR_MESSAGE_404


def get_user_avatar_controller(client, user_id, request):
    sub = verify_jwt(request)["sub"]

    user = client.get(client.key(USERS, user_id))
    if not user or user["sub"] != sub:
        raise AuthError(ERROR_MESSAGE_403, 403)

    file_name = f"{user_id}.png"
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(PHOTO_BUCKET)
    blob = bucket.blob(file_name)

    # No avatar exists
    if not blob.exists():
        return ERROR_MESSAGE_404, 404

    # Download the avatar to memory
    file_obj = io.BytesIO()
    blob.download_to_file(file_obj)
    file_obj.seek(0)

    return send_file(file_obj, mimetype="image/x-png", download_name=file_name), 200
