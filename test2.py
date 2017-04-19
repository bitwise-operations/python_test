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
        # time.sleep(2)
        # main_search.search_element("Xpath_search", "get_results")
        # main_search._click("tour_1")
        # main_search.switch_fr
        # main_search._click("look_cost")
        # time.sleep(2)
        # main_search._click("package_1")
        # main_search.switch_fr

        # self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.get('https://level.travel/packages/13961215')
        
        # main_search.cycle_for("Buyer")
        time.sleep(6)
        main_search.search_element("A", "surname_buyer")
        # main_search.data_entry("Buyer", "surname", "surname_buyer", "A")
        time.sleep(4)
        # main_search.data_entry("Buyer", "name", "name_buyer")

                

if __name__ == '__main__':
    unittest.main()