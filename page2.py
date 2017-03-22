from element import BaseSearchElement
from element import BaseSwitch
from element import ClickGoButton
from locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class Switch(BaseSwitch):
    pass

class Click(ClickGoButton):
    pass

class BasePage(object):

    def __init__(self, driver, conf=None, base_url=None):
        self.driver = driver
        self.conf = conf
        self.base_url = base_url

class MainSearch(BasePage):
    switch_fr = BaseSwitch()
    click = Click()
    print(click)
    
    # searchElement = BaseSearchElement()

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
        value1 = self.conf.get(section, option)
        self.locator = self.conf.get("Xpath_field", name_field)
        a = BaseSearchElement(self.locator)
        a = value1


    def search_element(self, section, option):
        self.locator = self.conf.get(section, option)
        a = BaseSearchElement(self.locator)





    




