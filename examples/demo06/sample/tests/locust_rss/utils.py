#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import inspect
import json
import sys

PY3 = True if sys.version_info[0] > 2 else False


def to_json(data):
    """
    解析json
    """
    res = str(data, encoding="utf-8") if PY3 else data.decode("utf-8")
    try:
        return json.loads(res)
    except:
        return {'status': -9999}


def post_request(client, data, url, func_name=None, **kw):
    """
    发起post请求
    """
    func_name = func_name if func_name else inspect.stack()[1][3]
    with client.post(url, data=data, name=func_name, catch_response=True, timeout=2, **kw) as response:
        result = response.content
        res = to_json(result)
        if res['status'] == 1:
            response.success()
        else:
            response.failure("%s-> %s" % ('error', result))
        return result
