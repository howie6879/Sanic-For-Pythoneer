#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from locust import TaskSet, task

import action


# 压力测试
class RssBehavior(TaskSet):
    @task(1)
    def interface_rss(self):
        action.action_rss(self.client)
