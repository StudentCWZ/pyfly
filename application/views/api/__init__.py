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

from flask import Flask

from application.views.api.api import api_bp


def register_api_views(app: Flask):
    app.register_blueprint(api_bp)
