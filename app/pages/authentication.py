from flask import Blueprint, render_template

authentication_bp = Blueprint("authentication_bp", __name__)


@authentication_bp.route("/authentication")
def show_authentication():
    return render_template("authentication.html")
