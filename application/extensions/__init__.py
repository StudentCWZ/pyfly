#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-03-09 08:57:20
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-07-14 21:57:56
# @Description: extensions
"""

from flask import Flask

from application.extensions.init_apispec import init_apispec
from application.extensions.init_bcrypt import flask_bcrypt
from application.extensions.init_cli import init_cli
from application.extensions.init_dynaconf import init_dynaconf
from application.extensions.init_jwt import jwt
from application.extensions.init_logger import init_logger
from application.extensions.init_migrate import init_migrate
from application.extensions.init_sqlalchemy import init_database


def init_plugs(app: Flask) -> None:
    init_dynaconf(app)
    init_logger(app)
    flask_bcrypt.init_app(app)
    jwt.init_app(app)
    init_database(app)
    init_apispec(app)
    init_migrate(app)
    init_cli(app)
