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
# @Description: auth controller
"""

from flask_loguru import logger

from application.dao import AuthDao
from application.utils.error import ParameterException


class AuthController:
    @classmethod
    def login(cls, dic: dict):
        """
        Authenticate user and return tokens by controller layer

        :param      cls:  The cls
        :type       cls:  { type_description }
        :param      dic:  The dic
        :type       dic:  dict
        """
        username = dic.get("username", None)
        password = dic.get("password", None)
        if not username or not password:
            logger.error("Missing username or password")
            raise ParameterException()
        return AuthDao.login(username, password)

    @classmethod
    def refresh(cls):
        """
        Revoke an access token by controller layer

        :param      cls:  The cls
        :type       cls:  { type_description }
        """
        return AuthDao.refresh()

    @classmethod
    def revoke_access_token(cls):
        """
        Revoke an access token by controller layer

        :param      cls:  The cls
        :type       cls:  { type_description }
        """
        return AuthDao.revoke_access_token()

    @classmethod
    def revoke_refresh_token(cls):
        """
        Revoke a refresh token by controller layer

        :param      cls:  The cls
        :type       cls:  { type_description }
        """
        return AuthDao.revoke_refresh_token()
