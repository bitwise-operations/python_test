#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from _configs._configs import Configs
from _configs._configs_css import Configs_css
from selenium.webdriver.chrome.options import Options


class Basic_settings(Configs, Configs_css):

    def __init__(self, *args, **kwargs):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=/Users/qa1/Library/Application\ Support/Google/Chrome",)
        options.add_argument("--profile-directory=qwe1")
        self.driver = webdriver.Chrome('/Users/qa1/pytest2/chromedriver', chrome_options=options)
        self.driver.implicitly_wait(50)

        Configs.__init__(self, *args, **kwargs)
        Configs_css.__init__(self, *args, **kwargs)
        self.configs()
        self.configs_css()

