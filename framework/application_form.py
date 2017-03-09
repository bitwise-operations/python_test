#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from basic_settings import Basic_settings
import time


class Application_form(Basic_settings):
    def __init__(self, *args, **kwargs):

        Basic_settings.__init__(self, *args, **kwargs)

    def choice_tour(self):
        driver = self.driver
        self.wait.until(self.EC.visibility_of_element_located
                                  ((self.By.ID, "search_results")))
        driver.find_element_by_xpath("//*[@id='search_results']/article[1]//a").click()
        time.sleep(2)
        self.wait.until(self.EC.visibility_of_element_located
                                  ((self.By.XPATH, "//*[text()='Посмотреть цены']")))
        driver.find_element_by_xpath("//*[text()='Посмотреть цены']").click()

    def appli_buyer(a):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='clientForm']//li[@class='"+a+"']//input").send_keys(a)

    def appli_form(self, section):
        driver = self.driver
        surname = self.conf.get(section, "surname")
        name = self.conf.get(section, "name")
        email = self.conf.get(section, "email")
        phone = self.conf.get(section, "phone")
        self.wait.until(self.EC.visibility_of_element_located
                                  ((self.By.ID, "clientForm")))
        appli_buyer(surname)
        appli_buyer(name)
        appli_buyer(email)
        appli_buyer(phone)
