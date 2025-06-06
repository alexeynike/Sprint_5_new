from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProfileLocators:
    LISTING_CARDS = (By.XPATH, "//div[@class='card']")




class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfileLocators()

    def assert_listing_cards_is_visible(self):
        self._find_element(*self.locators.LISTING_CARDS).is_displayed()