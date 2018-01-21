#!/usr/bin/env python
"""
 Created by howie.hu at 21/01/2018.
"""
import aiohttp

from sanic import Sanic
from sanic.response import text

app = Sanic()


async def get_news():
    """
    Sanic是一个异步框架，为了更好的发挥它的性能，有些操作最好也要用异步的
    比如这里发起请求就必须要用异步请求框架aiohttp
    所以使用本服务的时候请先执行:
    pip install aiohttp
    """
    pass


@app.route("/")
async def index(request):
    return text('Hello World!')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
