from flask import Blueprint, render_template

authorization_bp = Blueprint("authorization_bp", __name__)


@authorization_bp.route("/authorization")
def show_authorization():
    return render_template("authorization.html")
