#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
import time
from basic_settings import Basic_settings


class Test_form(Basic_settings, unittest.TestCase):
    def __init__(self, *args, **kwargs):
        Basic_settings.__init__(self, *args, **kwargs)
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_form(self):
        driver = self.driver
        driver.get('https://www.google.com/')

if __name__ == '__main__':
    unittest.main()