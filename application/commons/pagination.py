#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.4
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-01-06 10:10:45
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-07-14 21:50:36
# @Description: pagination 分页
"""

from flask import url_for, request

DEFAULT_PAGE_SIZE = 50
DEFAULT_PAGE_NUMBER = 1


def extract_pagination(page=None, per_page=None, **request_args):
    page = int(page) if page is not None else DEFAULT_PAGE_NUMBER
    per_page = int(per_page) if per_page is not None else DEFAULT_PAGE_SIZE
    return page, per_page, request_args


def paginate(query, schema):
    page, per_page, other_request_args = extract_pagination(**request.args)
    page_obj = query.paginate(page=page, per_page=per_page)
    next_ = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else page_obj.page,
        per_page=per_page,
        **other_request_args,
        **request.view_args
    )
    prev = url_for(
        request.endpoint,
        page=page_obj.prev_num if page_obj.has_prev else page_obj.page,
        per_page=per_page,
        **other_request_args,
        **request.view_args
    )

    return {
        "total": page_obj.total,
        "pages": page_obj.pages,
        "next": next_,
        "prev": prev,
        "results": schema.dump(page_obj.items),
    }
