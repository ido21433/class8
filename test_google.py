# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_title():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install())
    )

    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.quit()
