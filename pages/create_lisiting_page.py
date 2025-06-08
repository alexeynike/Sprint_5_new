import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage


class Locator:
    NAME_FIELD = (By.XPATH, "//input[@name='name']")
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@name='description']")
    PRICE_FIELD = (By.XPATH, "//input[@name='price']")
    CATEGORY_DROPDOWN_BTN = (By.XPATH, "//input[@name='category']/..//button")
    DROPDOWN_ITEMS = (By.XPATH, "//button[contains(@class, 'dropDownMenu_btn')]/span")
    CITY_DROPDOWN_BTN = (By.XPATH, "//input[@name='city']/..//button")
    PUBLISH_BTN = (By.XPATH, "//button[@type='submit']")


class CreateListingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locator()

    @allure.step("Создать объявление")
    def create_adw(self, name, category, city, description, price):
        self._send_keys(*self.locators.NAME_FIELD, name)
        self._click_element(*self.locators.CATEGORY_DROPDOWN_BTN)
        self.select_dropdown_item(self.locators.DROPDOWN_ITEMS, category)
        self._click_element(*self.locators.CITY_DROPDOWN_BTN)
        self.select_dropdown_item(self.locators.DROPDOWN_ITEMS, city)
        self._send_keys(*self.locators.DESCRIPTION_FIELD, description)
        self._send_keys(*self.locators.PRICE_FIELD, price)
        self._click_element(*self.locators.PUBLISH_BTN)
