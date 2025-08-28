from flask import Blueprint, request
from ..constants import USERS
from flasgger import swag_from
from ..controllers.users_controller import get_all_users_controller

get_all_users_bp = Blueprint("get_all_users_bp", __name__)


@get_all_users_bp.route(f"/{USERS}")
@swag_from("../../api/get_all_users.yml")
def get_all_users():
    return get_all_users_controller(request)
