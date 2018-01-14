#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from locust import HttpLocust

from locust_rss_http import RssBehavior
import action


class Rss(HttpLocust):
    host = action.HTTP_URL
    task_set = RssBehavior
    min_wait = 20
    max_wait = 3000
