#!/usr/bin/env python
from functools import wraps

from sanic.request import Request
from sanic import response

try:
    from ujson import loads as json_loads
    from ujson import dumps as json_dumps
except:
    from json import loads as json_loads
    from json import dumps as json_dumps

from src.config import CONFIG


def response_handle(request, dict_value, status=200):
    """
    根据request参数决定返回sanic.response 或者 json
    :param request: sanic.request.Request or dict
    :param dict_value:
    :return:
    """
    if isinstance(request, Request):
        return response.json(dict_value, status=status)
    else:
        return json_dumps(dict_value, ensure_ascii=False)


def authenticator(key):
    """

    :param keys: 验证方式 Api-Key : Magic Key
    :return: 返回值
    """

    def wrapper(func):
        @wraps(func)
        async def authenticate(request, *args, **kwargs):
            value = request.headers.get(key, None)
            if value and CONFIG.AUTH[key] == value:
                response = await func(request, *args, **kwargs)
                return response
            else:
                return response_handle(request, {'info': 'failed'}, status=401)

        return authenticate

    return wrapper


def auth_params(*keys):
    """
    api请求参数验证
    :param keys: params
    :return:
    """

    def wrapper(func):
        @wraps(func)
        async def auth_param(request=None, rpc_data=None, *args, **kwargs):
            request_params, params = {}, []
            if isinstance(request, Request):
                # sanic request
                if request.method == 'POST':
                    try:
                        post_data = json_loads(str(request.body, encoding='utf-8'))
                    except Exception as e:
                        return response_handle(request, {'info': 'error'})
                    else:
                        request_params.update(post_data)
                        params = [key for key, value in post_data.items() if value]
                elif request.method == 'GET':
                    request_params.update(request.args)
                    params = [key for key, value in request.args.items() if value]
                else:
                    return response_handle(request, {'info': 'error'})
            else:
                # gRPC request
                request_params = rpc_data
                params = [key for key, value in request_params.items() if value]

            if set(keys).issubset(set(params)):
                kwargs['request_params'] = request_params
                return await dec_func(func, request, *args, **kwargs)
            else:
                return response_handle(request, {'info': 'error'})

        return auth_param

    return wrapper


async def dec_func(func, request, *args, **kwargs):
    try:
        response = await func(request, *args, **kwargs)
        return response
    except Exception as e:
        return response_handle(request, {'info': 'error'})
