from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePageLocators:
    LOGIN_AND_REGISTER_BTN = (By.XPATH, "//button[text()='Вход и регистрация']")
    PLACE_ADW_BTN = (By.XPATH, "//button[text()='Разместить объявление']")
    NO_ACCOUNT_BTN = (By.XPATH, "//button[text()='Нет аккаунта']")
    LOGIN_FORM = (By.XPATH, "//div[contains(@class, 'homePage_modal')]//h1")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SUBMIT_PASSWORD_FIELD = (By.XPATH, "//input[@name='submitPassword']")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Создать аккаунт']")
    ERROR_MESSAGE = (By.XPATH, "//span[text()='Ошибка']")
    USER_LOGO_ICON = (By.XPATH, "//button[@class='circleSmall']")
    USER_EXIT_BTN = (By.XPATH, "//div[@class='columnSmall']/button")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")
    ADW_BLOCK = (By.XPATH, "//div[@class='card']")

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def open_home_page(self):
        self._open_url()

    def click_on_login_and_register_btn(self):
        self._click_element(*self.locators.LOGIN_AND_REGISTER_BTN)

    def register_user(self, email, password):
        self._click_element(*self.locators.NO_ACCOUNT_BTN)
        self._send_keys(*self.locators.EMAIL_FIELD, email)
        self._send_keys(*self.locators.PASSWORD_FIELD, password)
        self._send_keys(*self.locators.SUBMIT_PASSWORD_FIELD, password)
        self._click_element(*self.locators.CREATE_ACCOUNT_BTN)

    def login_user(self, email, password):
        self._send_keys(*self.locators.EMAIL_FIELD, email)
        self._send_keys(*self.locators.PASSWORD_FIELD, password)
        self._click_element(*self.locators.LOGIN_BTN)


    def assert_user_is_registered(self):
        self._find_element(*self.locators.USER_LOGO_ICON).is_displayed()
        assert self._find_element(*self.locators.USER_NAME).text == "User."

    def assert_user_is_not_registered(self):
        self._find_element(*self.locators.ERROR_MESSAGE).is_displayed()

    def logout_user(self):
        self._click_element(*self.locators.USER_EXIT_BTN)

    def assert_user_is_log_out(self):
        assert self._find_element(*self.locators.LOGIN_AND_REGISTER_BTN).is_displayed()

    def click_on_adw_btn(self):
        from pages.create_lisiting_page import CreateListingPage
        self._click_element(*self.locators.PLACE_ADW_BTN)
        return CreateListingPage(self.driver)

    def click_on_profile_logo(self):
        from pages.profile_page import ProfilePage
        self._click_element(*self.locators.USER_LOGO_ICON)
        return ProfilePage(self.driver)

    def assert_login_modal_is_displayed(self):
        assert self._find_element(*self.locators.LOGIN_FORM).text == "Чтобы разместить объявление, авторизуйтесь"

    def assert_is_home_page(self):
        self._find_element(*self.locators.ADW_BLOCK).is_displayed()
