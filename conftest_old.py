import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es', help="Choose language")


@pytest.fixture(scope="function")
def driver(request):
    user_language = request.config.getoption("language")
    print("\nstart driver for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit driver..")
    driver.quit()
