import allure

from pages.create_lisiting_page import CreateListingPage
from pages.home_page import HomePage
from helpers.email_generator import create_login
from pages.profile_page import ProfilePage


class TestCreateListing:
    @allure.title("Создать новое объявление")
    def test_create_adw(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.register_user(create_login(), "qwerty123")
        home_page.assert_user_is_registered()
        home_page.click_on_adw_btn()
        create_listing_page = CreateListingPage(browser)
        create_listing_page.create_adw("Test", "Книги", "Казань", "Описание", 999)
        home_page.assert_is_home_page()
        home_page.click_on_profile_logo()
        profile_page = ProfilePage(browser)
        profile_page.assert_listing_cards_is_visible()
