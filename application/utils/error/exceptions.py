#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-01-06 10:10:45
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-01-11 09:52:42
# @Description: 各种异常
"""

# pylint: skip-file

from application.utils.error.helper import APIException


class Success(APIException):
    code = 200
    msg = "ok"
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = "sorry, we made a mistake (*￣︶￣)!"
    error_code = 1500


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = "client is invalid"
    error_code = 1405


class ParameterException(APIException):
    code = 400
    msg = "invalid parameter"
    error_code = 1406


class NotFound(APIException):
    code = 404
    msg = "the resource are not found O__O..."
    error_code = 1404


class AuthFailed(APIException):
    code = 401
    error_code = 1401
    msg = "authorization failed"


class Forbidden(APIException):
    code = 403
    error_code = 1403
    msg = "forbidden, not in scope"
