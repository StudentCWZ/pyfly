#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-01-06 10:08:00
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-01-06 11:29:29
# @Description: 服务启动文件
"""

from application import create_app

app = create_app()


if __name__ == '__main__':
    app.run()

