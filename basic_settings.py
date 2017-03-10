#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from _configs._configs import Configs
from _configs._configs_css import Configs_css
from selenium.webdriver.chrome.options import Options


class Basic_settings(Configs):

    def __init__(self, *args, **kwargs):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=/Users/qa1/Library/Application\ Support/Google/Chrome",)
        options.add_argument("--profile-directory=qwe1")
        self.driver = webdriver.Chrome('/Users/qa1/pytest/chromedriver', chrome_options=options)
        self.driver.implicitly_wait(50)
        self.wait = WebDriverWait(self.driver, 60)
        self.By = By
        self.EC = EC

        Configs.__init__(self, *args, **kwargs)
        Configs_css.__init__(self, *args, **kwargs)
        self.configs()
        self.configs_css()

