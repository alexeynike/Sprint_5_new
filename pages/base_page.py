import random
from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = 'https://qa-desk.stand.praktikum-services.ru'

    def __init__(self, driver):
        self.driver = driver
        self._driver: ChromiumDriver = driver
        self.wait = WebDriverWait(self._driver, 10)

    def _open_url(self, endpoint=''):
        self._driver.get(self.BASE_URL + endpoint)

    def _scroll(self, x: int = 0, y: int = 0):
        return self._driver.execute_script(f"window.scroll({x}, {y})")

    def _find_element(self, by: str, locator: str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def _find_elements(self, by: str, locator: str) -> List[WebElement]:
        return self.wait.until(EC.visibility_of_any_elements_located((by, locator)))

    def _click_element(self, by, locator):
        self.wait.until(EC.element_to_be_clickable((by, locator))).click()

    def _send_keys(self, by, locator, text):
        self._find_element(by, locator).clear()
        self._find_element(by, locator).send_keys(text)

    def switch_tab(self):
        windows = self._driver.window_handles
        self._driver.switch_to.window(windows[-1])

    def assert_url_have(self, url):
        self.wait.until(EC.url_contains(url))

    def select_dropdown_item(self, element, name):
        items = self._find_elements(*element)
        for item in items:
            if item.text == name:
                item.click()
                break
        else:
            raise ValueError(f"Элемент выпадающего списка: {name} не найден")
