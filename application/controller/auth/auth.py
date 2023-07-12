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
# @Description: auth controller
"""

from flask import jsonify

from application.dao import AuthDao


class AuthController:
    @classmethod
    def login(cls, dic: dict):
        """
        Login controller

        :param      cls:  The cls
        :type       cls:  { type_description }
        :param      dic:  The dic
        :type       dic:  dict
        """
        username = dic.get("username", None)
        password = dic.get("password", None)
        if not username or not password:
            return jsonify({"msg": "Missing username or password"}), 400
        return AuthDao.login(username, password)
