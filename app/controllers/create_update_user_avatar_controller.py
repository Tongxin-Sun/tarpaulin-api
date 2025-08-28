from ..helpers.error import AuthError
from ..constants import ERROR_MESSAGE_400, ERROR_MESSAGE_403, USERS, PHOTO_BUCKET
from ..helpers.verify_jwt import verify_jwt
from google.cloud import datastore, storage

client = datastore.Client()


def create_update_user_avatar_controller(request, user_id):

    if "file" not in request.files:
        raise AuthError(ERROR_MESSAGE_400, 400)

    sub = verify_jwt(request)["sub"]

    user = client.get(client.key(USERS, user_id))
    if not user or user["sub"] != sub:
        raise AuthError(ERROR_MESSAGE_403, 403)

    file_obj = request.files["file"]
    storage_client = storage.Client()
    bucket = storage_client.bucket(PHOTO_BUCKET)
    blob = bucket.blob(f"{user_id}.png")
    file_obj.seek(0)
    blob.upload_from_file(file_obj)

    return {"avatar_url": request.base_url}, 200
