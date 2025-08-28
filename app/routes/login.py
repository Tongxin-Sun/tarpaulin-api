from flask import Blueprint, request, jsonify
from ..constants import USERS
from flasgger import swag_from
from ..controllers.login_controller import login_user_logic

login_bp = Blueprint("login_bp", __name__)


# User login endpoint
@login_bp.route(f"/{USERS}/login", methods=["POST"])
@swag_from("../../api/login.yml")
def login_user():
    content = request.get_json()
    id_token = login_user_logic(content)
    return jsonify(token=id_token), 200
