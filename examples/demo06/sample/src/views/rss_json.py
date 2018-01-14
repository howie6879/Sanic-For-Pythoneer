#!/usr/bin/env python
import sys

from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape
from sanic import Blueprint
from sanic.response import html, json

from src.config import CONFIG

# https://github.com/channelcat/sanic/blob/5bb640ca1706a42a012109dc3d811925d7453217/examples/jinja_example/jinja_example.py
# 开启异步特性  要求3.6+
enable_async = sys.version_info >= (3, 6)

json_bp = Blueprint('rss_json', url_prefix='json')
json_bp.static('/statics/rss_json', CONFIG.BASE_DIR + '/statics/rss_json')

# jinjia2 config
env = Environment(
    loader=PackageLoader('src.views.rss_json', '../templates/rss_json'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']),
    enable_async=enable_async)


async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    rendered_template = await template.render_async(**kwargs)
    return html(rendered_template)


@json_bp.route("/")
async def index(request):
    return await template('index.html')


@json_bp.route("/index")
async def rss_json(request):
    url = "http://blog.howie6879.cn/atom.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({"title": article["title_detail"]["value"], "link": article["link"]})
    return json(data)
