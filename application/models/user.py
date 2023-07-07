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
# @Description: user model
"""

from sqlalchemy.ext.hybrid import hybrid_property

from application.extensions.init_bcrypt import flask_bcrypt
from application.extensions.init_sqlalchemy import db


class User(db.Model):
    """Basic user model"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str):
        """return boolean"""
        # 判断传过来的密码是否与数据库存的密码一致
        return flask_bcrypt.check_password_hash(self._password, password)

    def __repr__(self) -> str:
        return "<User %s>" % self.username
