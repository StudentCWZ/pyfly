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
# @Description: user resources
"""

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from application.commons.pagination import paginate
from application.extensions.init_sqlalchemy import db
from application.models import User
from application.schemas import UserSchema
from application.utils.response import success_api


class UserResource(Resource):
    method_decorators = [jwt_required()]

    @staticmethod
    def get(user_id: int):
        schema = UserSchema()
        user = User.query.get_or_404(user_id)
        data = {"user": schema.dump(user)}
        return success_api(data=data)

    @staticmethod
    def put(user_id: int):
        schema = UserSchema(partial=True)
        user = User.query.get_or_404(user_id)
        user = schema.load(request.json, instance=user)

        db.session.commit()
        data = {"user": schema.dump(user)}
        return success_api(msg="user updated", data=data)

    @staticmethod
    def delete(user_id: int):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return success_api(msg="user deleted")


class UserList(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        schema = UserSchema(many=True)
        query = User.query
        data = paginate(query, schema)
        return success_api(data=data)

    def post(self):
        schema = UserSchema()
        user = schema.load(request.json)

        db.session.add(user)
        db.session.commit()

        data = {"user": schema.dump(user)}
        return success_api(msg="user created", data=data)
