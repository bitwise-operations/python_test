#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from basic_settings import Basic_settings
from selenium.common.exceptions import TimeoutException, WebDriverException
import time


class Main_search(Basic_settings):
    def __init__(self, *args, **kwargs):
        Basic_settings.__init__(self, *args, **kwargs)


    def s_form_lite(self, s_url, section):
        driver = self.driver
        departure_city = self.conf.get(section, "departure_city")
        country = self.conf.get(section, "country")
        date_depart = self.conf.get(section, "date_depart")
        nights = self.conf.get(section, "nights")
        adult = self.conf.get(section, "adult")
        kids = self.conf.get(section, "kids")

        data = "-".join([departure_city, "to", country, "departure", date_depart, "for", nights, "nights", adult, "adults", kids, "kids-1..5-stars"])
        _url = "/".join([self.base_url, s_url, data])
        driver.set_window_size(1920, 1080)
        driver.get(_url)
        self.choice(driver)

    def choice(self, driver):
        self.wait.until(self.EC.visibility_of_element_located
                                  ((self.By.ID, "search_results")))
        driver.find_element_by_xpath("//*[@id='search_results']/article[1]//a").click()
        time.sleep(2)

        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        
        self.wait.until(self.EC.visibility_of_element_located
                                  ((self.By.XPATH, "//*[text()='Посмотреть цены']")))
        driver.find_element_by_xpath("//*[text()='Посмотреть цены']").click()