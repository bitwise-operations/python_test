#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from basic_settings import Basic_settings
from _configs._configs import Configs
import time


class Application_form(Basic_settings):
    def __init__(self, *args, **kwargs):

        Basic_settings.__init__(self, *args, **kwargs)
        Configs.__init__(self, *args, **kwargs)
        self.configs()

    def choice_tour(self):
        driver = self.driver
        self.wait.until(self.EC.visibility_of_element_located
                                  ((self.By.ID, "search_results")))
        driver.find_element_by_xpath("//*[@id='search_results']/article[1]//a").click()
        time.sleep(2)

        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        
        self.wait.until(self.EC.visibility_of_element_located
                                  ((self.By.XPATH, "//*[text()='Посмотреть цены']")))
        driver.find_element_by_xpath("//*[text()='Посмотреть цены']").click()