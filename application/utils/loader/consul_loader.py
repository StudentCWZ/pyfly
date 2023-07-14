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
# @Description: consul loader
"""

from __future__ import annotations

import os
from typing import NamedTuple, Union

import yaml
from dynaconf.base import LazySettings
from dynaconf.utils import build_env_list
from dynaconf.utils.parse_conf import parse_conf_data

try:
    import consul
    from consul.base import ConsulException
except ImportError:
    raise ImportError(
        "consul package is not installed in your environment. "
        "`pip install python_consul` or disable the consul loader with "
    )


IDENTIFIER = "consul"


class SourceMetadata(NamedTuple):
    loader: str
    identifier: str
    env: str
    merged: bool = False


def get_client():
    _host = os.getenv('CONSUL_HOST', 'localhost')
    _port = os.getenv('CONSUL_PORT', 8500)
    _token = os.getenv('CONSUL_TOKEN')
    client = consul.Consul(host=_host, port=_port, token=_token)
    return client


def load(
    obj: LazySettings,
    env: str = None,
    silent: bool = True,
    key: str = None,
    validate=False,
) -> Union[bool, None]:
    _dc = os.environ.get('CONSUL_DC', 'dc1')
    _token = os.getenv('CONSUL_TOKEN')
    _key = os.getenv('CONSUL_KEY')
    if _key is None:
        raise RuntimeError(
            "CONSUL_KEY is not configured"
        )
    client = get_client()
    result = client.kv.get(key=_key, dc=_dc, token=_token)
    result = yaml.load(result[1]["Value"], Loader=yaml.FullLoader)
    source_metadata = SourceMetadata(IDENTIFIER, "unique", env)
    try:
        if result.get(env.upper()) is None:
            data = {
                key: parse_conf_data(value, tomlfy=True, box_settings=obj)
                for key, value in result.items()
            }
        else:
            data = {
                key: parse_conf_data(value, tomlfy=True, box_settings=obj)
                for key, value in result[env.upper()].items()
            }
        if data:
            obj.update(
                data,
                loader_identifier=source_metadata,
                validate=validate,
            )
    except Exception:
        if silent:
            return False
        raise
