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
# @Description: Logger 类定义
"""

# pylint: skip-file

import os
import sys
import time

from flask_loguru.compress import zip_logs
from loguru import logger

from .format import patching
from .macro import (
    k_log_enqueue,
    k_log_format,
    k_log_level,
    k_log_name,
    k_log_path,
    k_log_rotation,
    k_log_serialize,
)


class Logger:
    """This class is used to config loguru"""

    def __init__(self, app=None, config=None):
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")

        self.config = config

        if app is not None:
            self.init_app(app, config)

    def init_app(self, app, config=None):
        """This is used to initialize logger with your app object"""
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")

        base_config = app.config.copy()
        if self.config:
            base_config.update(self.config)
        if config:
            base_config.update(config)

        config = base_config

        config.setdefault(k_log_path, None)
        config.setdefault(k_log_name, "")
        config.setdefault(k_log_level, "DEBUG")
        config.setdefault(k_log_rotation, 60 * 60)
        config.setdefault(k_log_format, "")
        config.setdefault(k_log_enqueue, True)
        config.setdefault(k_log_serialize, True)

        self._set_loguru(app, config)

    def _set_loguru(self, app, config):
        """Config logru"""
        path = config[k_log_name]
        if config[k_log_path] is not None:
            path = os.path.join(config[k_log_path], config[k_log_name])

        level = config[k_log_level]
        _format = config[k_log_format] or patching

        def should_rotate(message, file):
            filepath = os.path.abspath(file.name)
            creation = os.path.getctime(filepath)
            now = message.record["time"].timestamp()
            return now - creation > config[k_log_rotation]

        def should_retention(logs):
            """检查是否需要进行压缩"""
            # 依次查找写入
            file_list = []
            for log in logs:
                file_path = os.path.abspath(log)

                if file_path.endswith(".zip"):
                    continue

                if time.gmtime(time.time() - os.path.getctime(file_path)).tm_mday == 7:
                    file_list.append(file_path)

            if file_list:
                zip_logs(config, file_list)

        logger.remove()
        # logger.add(path, level=level, format=_format, rotation=should_rotate,
        #            enqueue=config[k_log_enqueue], retention=should_retention)
        logger.add(sys.stderr, format=_format, level=level)

        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions.setdefault("loguru", {})
        app.extensions["loguru"][self] = logger
