from flask import Blueprint, request
from ..constants import USERS
from flasgger import swag_from
from ..controllers.get_a_user_controller import get_a_user_controller

get_a_user_bp = Blueprint("get_a_user_bp", __name__)


@get_a_user_bp.route(f"/{USERS}/<int:user_id>")
@swag_from("../../api/get_a_user.yml")
def get_a_user(user_id):
    return get_a_user_controller(request, user_id)
