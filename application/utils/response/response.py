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
# @Description: 自定义响应返回
"""


def success_api(msg: str = "ok", data: dict | None = None) -> dict:
    if data is None:
        data = {}
    resp = {"code": 200, "msg": msg, "error_code": 0, "data": data}
    return resp
