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
# @Description: auth dao
"""

from flask import jsonify, current_app
from flask_jwt_extended import create_access_token, create_refresh_token

from application.models import User
from application.dao.auth.helper import (
    add_token_to_database,
)


class AuthDao:
    @classmethod
    def login(cls, username: str, password: str):
        """
        Login Dao

        :param      cls:       The cls
        :type       cls:       { type_description }
        :param      username:  The username
        :type       username:  str
        :param      password:  The password
        :type       password:  str
        """
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return jsonify({"msg": "Bad credentials"}), 400

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        add_token_to_database(access_token, current_app.config["JWT_IDENTITY_CLAIM"])
        add_token_to_database(refresh_token, current_app.config["JWT_IDENTITY_CLAIM"])

        ret = {"access_token": access_token, "refresh_token": refresh_token}
        return jsonify(ret), 200
