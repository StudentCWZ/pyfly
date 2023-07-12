#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-01-06 10:32:46
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-01-06 10:33:20
# @Description: auth views
"""


from flask import request, Blueprint, current_app
from flask_loguru import logger
from flask_jwt_extended import jwt_required

from application.extensions.init_apispec import apispec
from application.controller import AuthController
from application.utils.error import ClientTypeError


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    """Authenticate user and return tokensr"""
    if not request.is_json:
        logger.error("Missing JSON in request")
        raise ClientTypeError()
    return AuthController.login(dic=request.json)


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """Refresh token"""
    return AuthController.refresh()


@auth_bp.route("/revoke_access", methods=["DELETE"])
@jwt_required()
def revoke_access_token():
    """Revoke an access token"""
    return AuthController.revoke_access_token()


@auth_bp.route("/revoke_refresh", methods=["DELETE"])
@jwt_required(refresh=True)
def revoke_refresh_token():
    """Revoke a refresh token, used mainly for logout"""
    return AuthController.revoke_refresh_token()


@auth_bp.before_app_first_request
def register_views():
    apispec.spec.path(view=login, app=current_app)
    apispec.spec.path(view=refresh, app=current_app)
    apispec.spec.path(view=revoke_access_token, app=current_app)
    apispec.spec.path(view=revoke_refresh_token, app=current_app)
