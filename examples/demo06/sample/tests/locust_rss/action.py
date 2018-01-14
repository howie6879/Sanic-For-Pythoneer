#!/usr/bin/env python
#  -*- coding: utf-8 -*-


import inspect
import json

from utils import post_request

HTTP_URL = "http://0.0.0.0:8000/v1/post/rss/"
GRPC_URL = "0.0.0.0:8990"


def json_requests(client, data, url):
    func_name = inspect.stack()[1][3]
    headers = {'content-type': 'application/json'}
    return post_request(client, data=json.dumps(data), url=url, func_name=func_name, headers=headers)


def action_rss(client):
    data = {
        "name": "howie6879"
    }
    json_requests(client, data, HTTP_URL)
