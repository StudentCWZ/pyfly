#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-01-06 10:34:07
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-01-06 10:34:52
# @Description: flask-dynaconf extension
"""

from dynaconf import FlaskDynaconf
from flask import Flask


def init_dynaconf(app: Flask) -> None:
    """
    Initialize the dynaconf extension

    :param app: flask.Flask application instance
    :return: None
    """
    FlaskDynaconf(
        app=app,
        core_loaders=[],
        settings_files=[],
        # envvar_prefix='EXAMPLE_ETL',
        # settings_files=_settings_files,  # load user configuration.
        # environments=True,  # Enable multi-level configuration，eg: default, development, production
        # load_dotenv=True,  # Enable load .env
        loaders=[
            "application.utils.loader.consul_loader",
            "dynaconf.loaders.env_loader",
        ],
        # lowercase_read=False,  # If true, can't use `settings.foo`, but can only use `settings.FOO`
        # includes=_external_files,  # Customs settings.
        # base_dir=_base_dir,  # `settings.BASE_DIR`
    )
