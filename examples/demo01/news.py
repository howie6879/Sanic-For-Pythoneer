#!/usr/bin/env python
"""
 Created by howie.hu at 21/01/2018.
"""
import aiohttp

from sanic import Sanic
from sanic.response import html

app = Sanic()


async def get_news(size=10):
    """
    Sanic是一个异步框架，为了更好的发挥它的性能，有些操作最好也要用异步的
    比如这里发起请求就必须要用异步请求框架aiohttp
    所以使用本服务的时候请先执行:
    pip install aiohttp
    数据使用的是readhub网站的api接口
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


@app.route("/")
async def index(request):
    html_tem = """
    <div style="width: 80%; margin-left: 10%">
        <p><a href="{href}" target="_blank">{title}</a></p>
        <p>{summary}</p>
         <p>{updated_at}</p>
    </div>
    """
    html_list = []
    # 获取数据
    all_news = await get_news()
    for each_news in all_news:
        html_list.append(html_tem.format(
            href=each_news.get('news_info', [{}])[0].get('url', '#'),
            title=each_news.get('title'),
            summary=each_news.get('summary'),
            updated_at=each_news.get('updated_at'),
        ))

    return html('<hr>'.join(html_list))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
