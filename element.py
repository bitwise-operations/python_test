from selenium.webdriver.support.ui import WebDriverWait


class BaseSearchElement(object):

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        driver.find_element_by_xpath(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        element = driver.find_element_by_xpath(self.locator)
        #return element.get_attribute("value")
        return element

class BaseSwitch(object):

    def __get__(self, obj, owner):
        driver = obj.driver
        for handle in driver.window_handles:
            driver.switch_to.window(handle)

class ClickGoButton(object):

    def __set__(self, obj, value):
        driver = obj.driver
        conf = obj.conf
        xpath = conf.get("Xpath_buttton", value)
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(xpath))
        element = driver.find_element_by_xpath(xpath)
        element.click()

