#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-01-06 10:32:46
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-07-14 22:02:17
# @Description: auth dao
"""

from flask import current_app, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt,
)
from flask_loguru import logger

from application.dao.auth.helper import add_token_to_database, revoke_token
from application.models import User
from application.utils import AuthFailed, success_api


class AuthDao:
    @classmethod
    def login(cls, username: str, password: str):
        """
        Authenticate user and return tokens by dao layer

        :param      cls:       The cls
        :type       cls:       { type_description }
        :param      username:  The username
        :type       username:  str
        :param      password:  The password
        :type       password:  str
        """
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            logger.error("Bad credentials")
            raise AuthFailed()

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        add_token_to_database(access_token, current_app.config["JWT_IDENTITY_CLAIM"])
        add_token_to_database(refresh_token, current_app.config["JWT_IDENTITY_CLAIM"])

        ret = {"access_token": access_token, "refresh_token": refresh_token}
        return success_api(ret)

    @classmethod
    def refresh(cls):
        """
        Get an access token from a refresh token by dao layer

        :param      cls:  The cls
        :type       cls:  { type_description }
        """
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        ret = {"access_token": access_token}
        add_token_to_database(access_token, current_app.config["JWT_IDENTITY_CLAIM"])
        return jsonify(ret), 200

    @classmethod
    def revoke_access_token(cls):
        """
        Revoke an access token by dao layer

        :param      cls:  The cls
        :type       cls:  { type_description }
        """
        jti = get_jwt()["jti"]
        user_identity = get_jwt_identity()
        revoke_token(jti, user_identity)
        return jsonify({"message": "token revoked"}), 200

    @classmethod
    def revoke_refresh_token(cls):
        """
        Revoke a refresh token by dao layer

        :param      cls:  The cls
        :type       cls:  { type_description }
        """
        jti = get_jwt()["jti"]
        user_identity = get_jwt_identity()
        revoke_token(jti, user_identity)
        return jsonify({"message": "token revoked"}), 200
