from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get("siteAddress")
driver.save_screenshot('screenshot.png')
soup = BeautifulSoup(driver.page_source,'html.parser' )
print(soup)
len(soup.select('.cd__wrapper'))
driver.quit()