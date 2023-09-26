import json
import os
from argparse import Namespace
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from utils.actions.login_page_actions import LoginPageActions
from utils.actions.main_page_actions import MainPageActions


@pytest.fixture(scope="session")
def driver() -> WebDriver:
    allure_path = ".allure_results"
    try:
        for file_name in os.listdir(allure_path):
            file_path = os.path.join(allure_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception:
        pass

    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def config():
    with open("env.json") as config_file:
        return Namespace(**json.load(config_file))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs["driver"]
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"screenshot_{datetime.today()}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as error:
            print(f"Failed to take screenshot: {error}")


@pytest.fixture(scope="session")
def main_page(driver, config):
    return MainPageActions(driver, config)


@pytest.fixture(scope="session")
def login_page(driver, config):
    return LoginPageActions(driver, config)
