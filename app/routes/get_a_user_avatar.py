from flask import Blueprint, request
from ..constants import USERS
from ..controllers.user_avatar_controller import get_user_avatar_controller
from google.cloud import datastore
from flasgger import swag_from

client = datastore.Client()

get_a_user_avatar_bp = Blueprint("get_a_user_avatar_bp", __name__)


# Get a user's avatar endpoint
@get_a_user_avatar_bp.route(f"/{USERS}/<int:user_id>/avatar")
@swag_from("../../api/get_a_user_avatar.yml")
def get_user_avatar(user_id):
    return get_user_avatar_controller(client, user_id, request)
