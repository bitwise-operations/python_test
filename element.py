from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        driver.find_element_by_xpath(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute("value")

class BaseSearchElement(object):

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        element = driver.find_element_by_xpath(self.locator)
        # return element.get_attribute("value")

class BaseSwitch(object):

    def __get__(self, obj, owner):
        driver = obj.driver
        for handle in driver.window_handles:
            driver.switch_to.window(handle)

class ClickGoButton(object):

    def __set__(self, obj, value):
        driver = obj.driver
        xpath = self.conf.get("Xpath_buttton", name_button)
        element = driver.find_element_by_xpath(xpath)
        element.click()

