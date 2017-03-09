#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Basic():
    def __init__(self, base_url, api, conf=None):
        self.base_url = base_url
        self.api = api
        self.conf = conf

    def base_add(self, *args, **kwargs):
        