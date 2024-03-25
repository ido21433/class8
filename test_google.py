# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_title():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install(), options=options)
    )

    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.quit()
