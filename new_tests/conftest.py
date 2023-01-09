import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Headless mode starts tests without UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1280,720')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://demoqa.com/text-box/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.close()  # закрывает вкладку
    driver.quit()  # закрывает браузер
    # driver.quite() # закрывает браузер, полностью
