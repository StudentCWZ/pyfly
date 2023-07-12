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
# @Description: format 自定义模块
"""

# pylint: skip-file

import json


def serialize(record: dict) -> str:
    time_stamp = record["time"]
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    subset = {
        "time": time_stamp,
        "message": record["message"],
        "level": record["level"].name.lower(),
        "tag": "{}:{}".format(record["file"].path, record["line"]),
        "field": {"data": record["extra"].get("data", {})},
    }
    return json.dumps(subset, ensure_ascii=False)


def patching(record: dict) -> str:
    record["extra"]["serialized"] = serialize(record)
    return "{extra[serialized]}\n"
