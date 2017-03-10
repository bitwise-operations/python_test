#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from basic_settings import Basic_settings
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.alert import Alert
from _configs._configs import Configs
import time

class Main_search(Basic_settings, Configs):
    def __init__(self, *args, **kwargs):
        Basic_settings.__init__(self, *args, **kwargs)
        Configs.__init__(self, *args, **kwargs)
        self.configs()

    def s_form_lite(self, s_url, section):
        driver = self.driver
        departure_city = self.conf.get(section, "departure_city")
        country = self.conf.get(section, "country")
        date_depart = self.conf.get(section, "date_depart")
        nights = self.conf.get(section, "nights")
        adult = self.conf.get(section, "adult")
        kids = self.conf.get(section, "kids")

        data = "-".join([departure_city, "to", country, "departure", date_depart, "for", nights, "nights", adult, "adults", kids, "kids-1..5-stars"])
        _url = "/".join([self.url, s_url, data])
        driver.set_window_size(1920, 1080)
        driver.get(_url)
