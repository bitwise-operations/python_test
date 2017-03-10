#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
import time
from _configs._configs import Configs
from steps.main_search import Main_search
from steps.application_form import Application_form


class Test_form(Configs, Main_search, Application_form, unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)   
        Configs.__init__(self, *args, **kwargs)
        Main_search.__init__(self, *args, **kwargs)
        Application_form.__init__(self, *args, **kwargs)
        
        self.configs()
        

    # def test_form(self):
    #     search = Main_search(self.base_url)
    #     new_s = search.s_form(self.country, self.nights, self.adult, self.departure_city)

    def test_form(self):
        # search_lite = Main_search(self.base_url)
        # new_s_lite = search_lite.s_form_lite(self.s_url, "Search_data_lite")
        # applic = Application_form()
        # new_choice = applic.choice_tour()
        #form = applic.appli_form("Buyer")
        self.s_form_lite(self.s_url, "Search_data_lite")


if __name__ == '__main__':
    unittest.main()
