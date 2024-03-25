from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def chrome():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    return driver


def test_title():
    driver = chrome()
    driver.get("https://google.com")
    assert "Google" in driver.title
    driver.close()

# just testing the webhook
#wow its working
