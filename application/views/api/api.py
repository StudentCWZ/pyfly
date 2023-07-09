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
# @Description: api views
"""

from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from application.extensions.init_apispec import apispec
from application.resources import UserResource
from application.schemas import UserSchema

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(api_bp)


api.add_resource(UserResource, "/users/<int:user_id>", endpoint="user_by_id")


@api_bp.before_app_first_request
def register_views():
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.path(view=UserResource, app=current_app)


@api_bp.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
