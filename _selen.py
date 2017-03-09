#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Selenium_v:
    def __init__(self, *args, **kwargs):
        pass

    def selen(self):
        self.driver = webdriver.Chrome('/Users/qa1/pytest/chromedriver')
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 50)
        driver = self.driver
        self.s_get = driver.get