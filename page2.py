from element import BaseSearchElement
from element import BaseSwitch
from locators import MainPageLocators
from selenium.webdriver.common.by import By

class SearchTextElement(BaseSearchElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = "//*[@id='search_results']"

class Switch(BaseSwitch):
    pass

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver, conf=None, base_url=None):
        self.driver = driver
        self.conf = conf
        self.base_url = base_url


class MainSearch(BasePage):

    search_text_element = SearchTextElement()
    switch_fr = BaseSwitch()

    def lite_search(self, s_url, section):
        driver = self.driver
        departure_city = self.conf.get(section, "departure_city")
        country = self.conf.get(section, "country")
        date_depart = self.conf.get(section, "date_depart")
        nights = self.conf.get(section, "nights")
        adult = self.conf.get(section, "adult")
        kids = self.conf.get(section, "kids")

        data = "-".join([departure_city, "to", country, "departure", date_depart, "for", nights, "nights", adult, "adults", kids, "kids-1..5-stars"])
        _url = "/".join([self.base_url, s_url, data])
        driver.get(_url)
        
    def click_go_button(self, name_button):
        """Triggers the search"""
        xpath = self.conf.get("Xpath_buttton", name_button)
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def data_entry(self, section, option, name_field):
        value_field = self.conf.get(section, option)
        xpath = self.conf.get("Xpath_field", name_field)
        self.driver.find_element(By.XPATH, xpath).send_keys(value_field)




