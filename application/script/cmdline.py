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
# @Description: cmdline
"""

import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from application.extensions.init_sqlalchemy import db
    from application.models import User

    click.echo("create user")
    user = User(username="StudentCWZ", email="StudentCWZ@outlook.com", password="qwe!2345", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
