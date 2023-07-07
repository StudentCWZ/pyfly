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
# @Description: views layer
"""

from flask import Flask

from application.views.api import register_api_views
from application.views.auth import register_auth_views


def init_view(app: Flask) -> None:
    register_auth_views(app)
    register_api_views(app)
