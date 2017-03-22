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
        main_search.lite_search(self.s_url, "Search_data_lite")
        main_search.search_element("Xpath_search", "get_results")
        # main_search.search_text_element
        main_search.click_go_button("tour_1")
        main_search.switch_fr
        main_search.click_go_button("look_cost")
        time.sleep(2)
        # main_search.click_go_button("package_1")
        print(main_search.click)
        main_search.click = "package_1"
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(3)
        main_search.data_entry("Buyer", "surname", "surname_buyer")
        time.sleep(2)
        main_search.search_element("Xpath_field", "surname_buyer")

        # self.driver.get("https://level.travel/packages/11759359")
        # main_search.data_entry("Buyer", "surname", "surname_buyer")
        # time.sleep(2)
        # main_search.search_element("Xpath_field", "surname_buyer")
                

if __name__ == '__main__':
    unittest.main()