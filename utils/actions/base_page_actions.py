import random
import time

import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePageActions:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.ELEMENT_VISIBLE_TIMEOUT = 10

    def _get_timeout(self, timeout=None):
        return self.ELEMENT_VISIBLE_TIMEOUT if timeout is None else timeout

    def _get_element_by_locator(self, locator):
        wait = WebDriverWait(self.driver, self._get_timeout())
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def _get_elements_by_locator(self, locator):
        wait = WebDriverWait(self.driver, self._get_timeout())
        elements = wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    @allure.step("Open page")
    def open_page(self, url):
        self.driver.get(self.config.base_url + url)

    @allure.step("Check url")
    def check_url(self, expected_url):
        current_url = self.driver.current_url
        assert expected_url in current_url, f"Current URL {current_url} does not match the expected URL {expected_url}"

    @allure.step("Check element visibility")
    def is_element_visible(self, expected_element, timeout=None):
        try:
            WebDriverWait(self.driver, self._get_timeout(timeout)).until(
                EC.visibility_of_element_located(expected_element)
            )
        except Exception as e:
            pytest.fail(f"Element {expected_element} not found or not visible after "
                        f"{self._get_timeout(timeout)} sec. Error: {str(e)}")

    @allure.step("Scroll to the bottom of a page")
    def scroll_to_bottom(self, timeout=None):
        timeout = self._get_timeout(timeout)
        start_time = time.time()
        is_scrolled = False

        body_element = self.driver.find_element(By.CSS_SELECTOR, ".main-body")

        while time.time() - start_time < timeout and not is_scrolled:
            try:
                body_element.send_keys(Keys.PAGE_DOWN)
                self.driver.find_element(By.CSS_SELECTOR, "div.feed__loader")
            except Exception:
                footer = self.driver.find_element(By.CSS_SELECTOR, "footer.footer")
                assert footer, "After scroll to page end element footer does not found"
                self.driver.execute_script("arguments[0].scrollIntoView();", footer)
                is_scrolled = True

        if not is_scrolled:
            pytest.fail(f"After {self._get_timeout(timeout)} sec, the page was not scrolled to the end")

    @allure.step("Wait for clickable element")
    def wait_for_clickable_element(self, locator, timeout=None):
        timeout = self._get_timeout(timeout)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            pytest.fail(f"After {self._get_timeout(timeout)} sec, the element {locator} did not become clickable")

    @allure.step("Click element")
    def click_element(self, locator):
        element = self._get_element_by_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Get text from random element")
    def get_text_from_random_elements(self, locator):
        elements = self._get_elements_by_locator(locator)

        if not elements:
            pytest.fail(f"Incorrect locator: {locator}, no elements found")

        random_element = random.choice(elements)
        return random_element.text

    @allure.step("Fill input field")
    def fill_input_field(self, locator, text_to_enter):
        input_field = self._get_element_by_locator(locator)
        input_field.clear()
        input_field.send_keys(text_to_enter)

    @allure.step("Check a element contains text")
    def check_element_contains_text(self, locator, expected_text):
        element = self._get_element_by_locator(locator)

        actual_text = element.text.strip()
        assert actual_text.lower() == expected_text.lower(), \
            f"Expected text: {expected_text}, but actual: {actual_text}"

    @allure.step("Check any element contains text")
    def check_any_element_contains_text(self, locator, expected_text):
        is_found = False

        elements = self._get_elements_by_locator(locator)

        for element in elements:
            actual_text = element.text.strip()
            if expected_text.lower() in actual_text.lower():
                is_found = True
                break

        if not is_found:
            pytest.fail(f"Element: {locator} with text: {expected_text} not found")

    @allure.step("Switch to new window")
    def switch_to_new_window(self):
        all_windows = self.driver.window_handles
        new_window = all_windows[-1]

        self.driver.switch_to.window(new_window)

    @allure.step("Close current window")
    def close_current_window(self):
        self.driver.close()
