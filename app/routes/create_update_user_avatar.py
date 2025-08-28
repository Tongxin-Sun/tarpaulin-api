from flask import Blueprint, request
from flasgger import swag_from
from ..constants import USERS
from ..controllers.create_update_user_avatar_controller import (
    create_update_user_avatar_controller,
)

create_update_user_avatar_bp = Blueprint("create_update_user_avatar_bp", __name__)


@create_update_user_avatar_bp.route(f"/{USERS}/<int:user_id>/avatar", methods=["POST"])
@swag_from("../../api/create_update_user_avatar.yml")
def create_update_user_avatar(user_id):
    return create_update_user_avatar_controller(request, user_id)
