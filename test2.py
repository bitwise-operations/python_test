#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from basic import Basic_settings
import page2
import time


class Test_form(Basic_settings, unittest.TestCase):
    def __init__(self, *args, **kwargs):
        Basic_settings.__init__(self, *args, **kwargs)    
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_form(self):
        main_search = page2.MainSearch(self.driver, self.conf, self.base_url)
        # main_search.lite_search(self.s_url, "Search_data_lite")
        # self.driver.maximize_window()
        # main_search.search_element("Xpath_search", "get_results")
        # time.sleep(2)
        # main_search._click("tour_1")
        # main_search.switch_fr
        # main_search._click("look_cost")
        # time.sleep(3)
        # main_search._click("package_1")
        # time.sleep(2)
        # main_search.switch_fr

        # self.driver.switch_to.window(self.driver.window_handles[2])

        # main_search.cycle_for("Buyer")
        self.driver.get("https://level.travel/packages/15220226")
        a = self.driver.find_elements_by_xpath("//*[@id='clientForm']//input")
        print(len(a))
        for i in range(len(a), 1):
            b = str(i)
            self.driver.find_elements_by_xpath("//*[@id='clientForm']//input"+[b].clear()

        # self.driver.save_screenshot('eyetest.png')
        # main_search.cycle_for("Buyer")
        # main_search.data_entry("Buyer", "surname", "surname_buyer", "A")

        # main_search.data_entry("Buyer", "name", "name_buyer")
        time.sleep(10)

                

if __name__ == '__main__':
    unittest.main()