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


from flask import request, jsonify, Blueprint, current_app

from application.extensions.init_apispec import apispec
from application.controller import AuthController


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    return AuthController.login(dic=request.json)


@auth_bp.before_app_first_request
def register_views():
    apispec.spec.path(view=login, app=current_app)
