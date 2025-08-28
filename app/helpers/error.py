from flask import Blueprint, jsonify


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


err_bp = Blueprint("err_bp", __name__)


def register_error_handlers(app):
    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response
