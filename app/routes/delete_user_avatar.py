from flask import Blueprint, request
from ..constants import USERS
from flasgger import swag_from
from ..controllers.delete_user_avatar_controller import delete_user_avatar_controller

delete_user_avatar_bp = Blueprint("delete_user_avatar_bp", __name__)


# Delete a user's avatar endpoint
@delete_user_avatar_bp.route(f"/{USERS}/<int:user_id>/avatar", methods=["DELETE"])
@swag_from("../../api/delete_user_avatar.yml")
def delete_user_avatar(user_id):
    return delete_user_avatar_controller(request, user_id)
