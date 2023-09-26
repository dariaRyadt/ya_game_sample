import allure
import pytest

from utils.page_objects.main_page import MainPagePageObject


@allure.suite("Main Page")
class TestMainPage:

    @allure.title("Open main page")
    def test_open_main_page(self, main_page):
        main_page.open_page("/")
        main_page.check_url("yandex.ru/games/")

    @allure.title("Check header elements")
    @pytest.mark.parametrize("element_name", MainPagePageObject.header_elements.keys())
    def test_check_header_elements(self, main_page, element_name):
        locator = MainPagePageObject.header_elements[element_name]
        main_page.is_element_visible(locator)

    @allure.title("Check category elements")
    @pytest.mark.parametrize("element_name", MainPagePageObject.category_elements.keys())
    def test_check_category_elements(self, main_page, element_name):
        locator = MainPagePageObject.category_elements[element_name]
        main_page.is_element_visible(locator)

    @allure.title("Check tags elements")
    @pytest.mark.parametrize("element_name", MainPagePageObject.tags_elements.keys())
    def test_check_tags_elements(self, main_page, element_name):
        locator = MainPagePageObject.tags_elements[element_name]
        main_page.is_element_visible(locator)

    @allure.title("Check sections")
    @pytest.mark.parametrize("element_name", MainPagePageObject.sections_elements.keys())
    def test_check_sections_elements(self, main_page, element_name):
        main_page.scroll_to_bottom(120)
        locator = MainPagePageObject.sections_elements[element_name]
        main_page.is_element_visible(locator)

    @allure.title("Check footer elements")
    @pytest.mark.parametrize("element_name", MainPagePageObject.footer_elements.keys())
    def test_check_footer_elements(self, main_page, element_name):
        main_page.scroll_to_bottom(120)
        locator = MainPagePageObject.footer_elements[element_name]
        main_page.is_element_visible(locator)

    @allure.title("Search game by name and check result")
    def test_search_by_game_name(self, main_page):
        random_game_name = main_page.get_text_from_random_elements(locator=MainPagePageObject.game_title)

        main_page.fill_input_field(
            locator=MainPagePageObject.header_elements["search_input"],
            text_to_enter=random_game_name
        )
        main_page.is_element_visible(MainPagePageObject.find_button)
        main_page.click_element(MainPagePageObject.find_button)

        main_page.check_element_contains_text(
            locator=MainPagePageObject.search_result_title,
            expected_text=f"Результаты поиска по запросу: «{random_game_name}»"
        )
        main_page.check_any_element_contains_text(
            locator=MainPagePageObject.game_title,
            expected_text=random_game_name
        )
