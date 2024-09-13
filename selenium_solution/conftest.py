"""Module containing the configuration for the pytest"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.firefox.service import Service as firefoxservice
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture()
def setup(request,get_arguments):
    """Method to define the process during setup  and tear down"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = get_arguments
    if browser == 'chrome':
        driver = webdriver.Chrome(service= chromeservice(ChromeDriverManager().install()),options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=firefoxservice(GeckoDriverManager().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get('http://127.0.0.1:56563')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    """Method to add additoinal options to pytest"""
    parser.addoption("--browser",action="store",default="chrome")

@pytest.fixture(scope="session")
def get_arguments(request):
    """Method to retrive the arguments passed by the user"""
    browser_ = request.config.getoption("--browser")
    return browser_

