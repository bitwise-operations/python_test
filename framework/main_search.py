#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from basic_settings import Basic_settings
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.alert import Alert
import time


class Main_search(Basic_settings):
    def __init__(self, *args, **kwargs):
        self.url = args[0]

        Basic_settings.__init__(self, *args, **kwargs)

    def s_form(self, country, nights, adult, departure_city, kids=None):
        driver = self.driver
        xpath = driver.find_element_by_xpath
        driver.get(self.url)

        driver.maximize_window()
        self.wait.until(self.EC.visibility_of_element_located
                                ((self.By.CLASS_NAME, self.search_form)))
        xpath(self.xpath_country).send_keys(country)
        xpath(self.xpath_tabindex2).click()
        self.wait.until(self.EC.visibility_of_element_located
                                ((self.By.XPATH, self.xpath_date)))
        driver.find_elements_by_xpath(self.xpath_date)[0].click()

        a = xpath(self.xpath_person_t).text
        xpath(self.xpath_person).click()
        y = int(nights)
        z = int(a[0]) - y
        if z > 0:
            for i in range(z):
                xpath(self.xpath_person + self.xpath_subtract).click()
        elif z < 0:
            for i in range(abs(z)):
                xpath(self.xpath_person + self.xpath_add).click()
        else:
            pass

        y = 1
        a = xpath(self.xpath_tabindex4 + self.xpath_f_i).text
        xpath(self.xpath_tabindex4).click()
        y = 1
        z = int(a[0]) - y
        if z > 0:
            for i in range(z):
                xpath(self.xpath_tabindex4 + self.xpath_subtract).click()
        elif z < 0:
            for i in range(abs(z)):
                xpath(self.xpath_tabindex4 + self.xpath_add).click()                
        else:
            pass

        add_kids = 3,
        xpath(self.xpath_tabindex4 + self.xpath_kids_a).click()
        for i in range(len(add_kids)):
            xpath(self.xpath_tabindex4 + self.xpath_kids_a + "//option[@value='"+ str(add_kids[i]) +"']").click()

        xpath(self.xpath_tabindex5).click()
        xpath(self.xpath_tabindex5 +"/input").send_keys(departure_city)
        xpath("//div[@class='"+ self.search_submit +"']/*/span[text()='Найти']/..").click()

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
        time.sleep(1)
        # try:
        #     self.wait.until(self.EC.visibility_of_element_located
        #                         ((self.By.CLASS_NAME, self.search_filt_pow)))
        #     driver.find_element_by_xpath(self.xpath_b_thanks).click()
        # except WebDriverException:
        #     pass

        self.wait.until(self.EC.visibility_of_element_located
                                  ((self.By.ID, "search_results")))
        driver.find_element_by_xpath("//*[@id='search_results']/article[1]//a").click()

        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        
        self.wait.until(self.EC.visibility_of_element_located
                                ((self.By.XPATH, "//*[text()='Посмотреть цены']")))
        driver.find_element_by_xpath("//*[text()='Посмотреть цены']").click()
        
