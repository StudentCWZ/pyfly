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
# @Description: create_app
"""

import os

from flask import Flask

from application.extensions import init_plugs
from application.views import init_view


def create_app(config_name=None):
    """The function of factory with app.

    Args:
        config_name (_type_, optional): about config name. Defaults to None.

    Returns:
        _type_: None
    """
    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

    if not config_name:
        # 尝试从本地环境中读取
        config_name = os.getenv('Flask_ENV', 'development')

    # 设置 dynaconf 相关环境变量
    os.environ['ENV_FOR_DYNACONF'] = config_name

    # 引入数据库配置
    # app.config.from_object(config[config_name])

    # 注册各种插件
    init_plugs(app)

    # 注册路由
    init_view(app)

    # # 注册命令
    # init_script(app)

    return app
