#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-07-09 08:57:20
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-07-09 08:58:26
# @Description: version 测试封装模块
"""


from application import __version__


def test_version():
    """Test version"""
    assert __version__ == '0.1.0'
