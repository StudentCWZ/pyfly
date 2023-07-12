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
# @Description: 自定义异常
"""

# pylint: skip-file

from flask import json, request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = "sorry, we made a mistake (*￣︶￣)!"
    error_code = 1500
    data = {}

    def __init__(self, msg=None, code=None, error_code=None, data=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        if data:
            self.data = data
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None, scope=None):
        data = self.data or {"request": request.method + " " + self.get_url_no_param()}
        body = dict(code=self.code, msg=self.msg, error_code=self.error_code, data=data)
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None, scope=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json")]

    @staticmethod
    def get_url_no_param():
        """Get no param url"""
        full_path = str(request.full_path)
        main_path = full_path.split("?")
        return main_path[0]
