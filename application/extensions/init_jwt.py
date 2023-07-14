#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.10.6
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-01-06 10:32:46
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-07-14 22:01:56
# @Description: flask_jwt_extended extension
"""

from flask_jwt_extended import JWTManager

from application.dao.auth.helper import is_token_revoked
from application.models import User

jwt = JWTManager()


@jwt.user_lookup_loader
def user_loader_callback(jwt_headers, jwt_payload):
    identity = jwt_payload["sub"]
    return User.query.get(identity)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_headers, jwt_payload):
    return is_token_revoked(jwt_payload)
