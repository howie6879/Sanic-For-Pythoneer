#!/usr/bin/env python
"""
 Created by howie.hu at 21/01/2018.
"""
import aiohttp
import random

from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.response import html, json, redirect

app = Sanic()


async def get_news(size=10):
    """
    Sanic是一个异步框架，为了更好的发挥它的性能，有些操作最好也要用异步的
    比如这里发起请求就必须要用异步请求框架aiohttp
    所以使用本服务的时候请先执行: pip install aiohttp
    数据使用的是readhub网站的api接口
    为了使这个数据获取函数正常运行，我会保持更新，所以具体代码见 examples/demo01/news.py
    """
    all_news, readhub_api = [], "https://api.readhub.me/topic"
    try:
        async with aiohttp.ClientSession() as client:
            headers = {'content-type': 'application/json'}
            params = {'pageSize': size}
            async with client.get(readhub_api, params=params, headers=headers) as response:
                assert response.status == 200
                result = await response.json()

            for value in result.get('data', []):
                each_data = {}
                each_data['title'] = value.get('title')
                each_data['summary'] = value.get('summary')
                each_data['news_info'] = value.get('newsArray')
                each_data['updated_at'] = value.get('updatedAt')
                all_news.append(each_data)
            return all_news
    except Exception as e:
        return all_news


@app.route("/<page:int>")
@app.route("/")
async def index(request, page=1):
    # html页面模板
    html_tem = """
    <div style="width: 80%; margin-left: 10%">
        <p><a href="{href}" target="_blank">{title}</a></p>
        <p>{summary}</p>
         <p>{updated_at}</p>
    </div>
    """
    html_list = []
    # 获取数据
    all_news = await get_news(page * 10)
    # 生成在浏览器展示的html页面
    for each_news in all_news:
        html_list.append(html_tem.format(
            href=each_news.get('news_info', [{}])[0].get('url', '#'),
            title=each_news.get('title'),
            summary=each_news.get('summary'),
            updated_at=each_news.get('updated_at'),
        ))
    result = html_list[(page - 1) * 10:]
    if result:
        return html('<hr>'.join(result))
    else:
        return html('<hr>'.join(html_list))


@app.route('/json')
async def index_json(request):
    """
    默认返回一条资讯，最多十条
    """
    nums = request.args.get('nums', 1)
    # 获取数据
    all_news = await get_news()
    try:
        return json(random.sample(all_news, int(nums)))
    except ValueError:
        return json(all_news)


@app.exception(NotFound)
def ignore_404s(request, exception):
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
