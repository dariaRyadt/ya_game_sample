import allure

from utils.page_objects.login_page import LoginPagePageObject
from utils.page_objects.main_page import MainPagePageObject


@allure.suite("Login Page")
class TestLoginPage:

    @allure.title("Open login page")
    def test_open_login_page(self, login_page):
        login_page.open_page("/")
        login_page.check_url("yandex.ru/games/")
        login_page.click_element(MainPagePageObject.header_elements["login_button"])
        login_page.check_url("passport.yandex.ru/auth")

        login_page.check_login_form_elements()

    @allure.title("Fill fake credentials")
    def test_fill_fake_credentials(self, login_page, config):
        login_page.fill_input_field(locator=LoginPagePageObject.email_input, text_to_enter=config.email)
        login_page.click_element(LoginPagePageObject.sign_in_button)

        login_page.fill_input_field(locator=LoginPagePageObject.password_input, text_to_enter=config.password)
        login_page.click_element(LoginPagePageObject.sign_in_button)

        login_page.is_element_visible(LoginPagePageObject.auth_error_label)
        login_page.click_element(LoginPagePageObject.back_to_email_button)

    @allure.title("Check login by vk")
    def test_check_login_by_vk(self, login_page):
        login_page.is_element_visible(LoginPagePageObject.auth_social_title)
        login_page.wait_for_clickable_element(LoginPagePageObject.auth_by_vk_button)
        login_page.click_element(LoginPagePageObject.auth_by_vk_button)
        login_page.check_auth_url_in_new_window("id.vk.com/auth")
