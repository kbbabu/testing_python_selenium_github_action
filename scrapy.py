#source for this code - https://github.com/adilshehzad786/Python-Selenium-GitHub-Actions/blob/main/scraper.py
#https://github.com/MarketingPipeline/Python-Selenium-Action/blob/main/Selenium-Template.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
#from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
#driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

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
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://github.com')
print(driver.title)

driver.stop_client()
driver.close()
driver.quit()







