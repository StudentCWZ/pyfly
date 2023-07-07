#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-03-09 08:57:20
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-03-09 08:58:26
# @Description: flask-sqlalchemy extension
"""

from flask import Flask
from flask_migrate import Migrate

from application.extensions.init_sqlalchemy import db

migrate = Migrate()


def init_migrate(app: Flask) -> None:
    """
    Initialize the database extension

    :param app: flask.Flask application instance
    :return: None
    """
    migrate.init_app(app, db)