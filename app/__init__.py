from flask import Flask
from .pages.main import main_bp
from .pages.authorization import authorization_bp
from .pages.authentication import authentication_bp
from .routes.login import login_bp
from flasgger import Swagger
from .helpers.error import register_error_handlers
from .routes.get_all_users import get_all_users_bp
from .routes.get_a_user import get_a_user_bp
from .routes.create_update_user_avatar import create_update_user_avatar_bp
from .routes.get_a_user_avatar import get_a_user_avatar_bp
from .routes.delete_user_avatar import delete_user_avatar_bp
from .routes.create_course import create_course_bp
from .routes.get_courses import get_courses_bp
from .routes.get_course import get_course_bp
from .routes.update_course import update_course_bp
from .routes.delete_course import delete_course_bp
from .routes.update_enrollment import update_enrollment_bp
from .routes.get_enrollments import get_enrollments_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(authorization_bp)
    app.register_blueprint(authentication_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(get_all_users_bp)
    app.register_blueprint(get_a_user_bp)
    app.register_blueprint(create_update_user_avatar_bp)
    app.register_blueprint(get_a_user_avatar_bp)
    app.register_blueprint(delete_user_avatar_bp)
    app.register_blueprint(create_course_bp)
    app.register_blueprint(get_courses_bp)
    app.register_blueprint(get_course_bp)
    app.register_blueprint(update_course_bp)
    app.register_blueprint(delete_course_bp)
    app.register_blueprint(update_enrollment_bp)
    app.register_blueprint(get_enrollments_bp)
    register_error_handlers(app)

    swagger_template = {
        "swagger": "2.0",
        "info": {"title": "Tarpaulin API", "version": "1.0"},
        "tags": [
            {
                "name": "User Login",
                "description": "Endpoints for user login and authentication",
            },
            {"name": "Users", "description": "Endpoints for user management"},
            {"name": "Course", "description": "Endpoints for courses and enrollments"},
        ],
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "tarpaulin_api",
                "route": "/tarpaulin_api.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",  # important
        "swagger_ui": True,
        "specs_route": "/docsapi/",
    }

    swagger = Swagger(app, template=swagger_template, config=swagger_config)
    return app
