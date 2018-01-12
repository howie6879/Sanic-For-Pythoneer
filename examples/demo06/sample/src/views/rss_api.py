#!/usr/bin/env python
import asyncio

from aiocache import cached, RedisCache
from aiocache.serializers import PickleSerializer
from feedparser import parse
from sanic import Blueprint
from sanic.response import json

try:
    from ujson import loads as json_loads
except:
    from json import loads as json_loads

from src.tools.mid_decorator import auth_params

api_bp = Blueprint('rss_api', url_prefix='v1')


@cached(ttl=1000, cache=RedisCache, key="rss", serializer=PickleSerializer(), port=6379, namespace="main")
async def get_rss():
    print("Sleeping for three seconds zzzz.....")
    await asyncio.sleep(3)
    url = "http://blog.howie6879.cn/atom.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({"title": article["title_detail"]["value"], "link": article["link"]})
    return data


@api_bp.route("/get/rss/<name>")
async def get_rss_json(request, name):
    if name == 'howie6879':
        data = await get_rss()
        return json(data)
    else:
        return json({'info': '请访问 http://0.0.0.0:8000/v1/get/rss/howie6879'})


@api_bp.route("/post/rss/", methods=['POST'])
@auth_params('name')
async def post_rss_json(request, **kwargs):
    post_data = json_loads(str(request.body, encoding='utf-8'))
    name = post_data.get('name')
    if name == 'howie6879':
        data = await get_rss()
        return json(data)
    else:
        return json({'info': '参数错误'})
