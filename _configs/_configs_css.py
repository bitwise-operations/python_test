#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import configparser
from os import path


class Configs_css:
    def __init__(self, *args, **kwargs):
        pass

    def configs_css(self):
        self.conf = configparser.RawConfigParser()
        self.conf.read(path.abspath('./_configs/text_css.ini'))
        self.search_form = self.conf.get("Class_css", "search_form")
        self.search_submit = self.conf.get("Class_css", "search_submit")
        self.search_dete = self.conf.get("Class_css", "search_dete")
        self.xpath_country = self.conf.get("Xpath", "xpath_country")
        self.xpath_tabindex2 = self.conf.get("Xpath", "xpath_tabindex2")
        self.xpath_date = self.conf.get("Xpath", "xpath_date")
        self.xpath_person_t = self.conf.get("Xpath", "xpath_person_t")
        self.xpath_person = self.conf.get("Xpath", "xpath_person")
        self.xpath_subtract = self.conf.get("Xpath", "xpath_subtract")
        self.xpath_add = self.conf.get("Xpath", "xpath_add")
        self.xpath_tabindex4 = self.conf.get("Xpath", "xpath_tabindex4")
        self.xpath_tabindex5 = self.conf.get("Xpath", "xpath_tabindex5")
        self.xpath_f_i = self.conf.get("Xpath", "xpath_f_i")
        self.xpath_kids_a = self.conf.get("Xpath", "xpath_kids_a")
        self.search_filt_pow = self.conf.get("Class_css", "search_filt_pow")
        self.xpath_b_thanks = self.conf.get("Xpath", "xpath_b_thanks")