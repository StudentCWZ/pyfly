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
# @Description: logger 插件
"""


from flask import Flask

from src.app.libs import Logger

log = Logger()


def init_logger(app: Flask) -> None:
    """
    Initialize the logger

    :param app: flask.Flask application instance
    :return: None
    """
    log.init_app(app, {"LOG_LEVEL": app.config.LOGGER.LEVEL})
