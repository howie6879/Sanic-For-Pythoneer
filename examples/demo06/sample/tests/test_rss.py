#!/usr/bin/env python
"""
 Created by howie.hu at 03/11/2017.
"""
import asyncio
import os
import sys

import pytest
import ujson
import uvloop

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import run

import setting

grpc = pytest.mark.skipif(
    setting.DIS_GRPC_TEST,
    reason="need set DIS_GRPC_TEST=False option to run"
)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


@pytest.yield_fixture
def app():
    yield run.app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))


@pytest.yield_fixture
def loop():
    loop = asyncio.get_event_loop()
    yield loop


async def test_http_rss(test_cli):
    data = setting.rss_data()
    response = await test_cli.post('/v1/post/rss/', data=ujson.dumps(data))
    resp_json = await response.json()
    assert resp_json['status'] == 1


@grpc
def test_grpc_rss():
    pass
