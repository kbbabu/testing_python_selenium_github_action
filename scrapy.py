#source for this code - https://github.com/adilshehzad786/Python-Selenium-GitHub-Actions/blob/main/scraper.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_servie = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
  chrome_options.add_arguments(option)

driver = webdriver.Chrome(service = chrome_service, options = chrome_options)

driver.get('http://nytimes.com')
print(driver.title)
driver.stop_client()
driver.close()
driver.quit()



