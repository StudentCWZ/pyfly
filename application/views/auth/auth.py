from flask import request, jsonify, Blueprint, current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)

from application.models import User
from application.extensions.init_apispec import apispec


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400
    ret = {"msg": "ok"}
    print(current_app.config.SQLALCHEMY_DATABASE_URI)
    return jsonify(ret), 200


@auth_bp.before_app_request
def register_views():
    apispec.spec.path(view=login, app=current_app)
