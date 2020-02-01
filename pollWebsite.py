import time

from bs4 import BeautifulSoup as bs
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

searchTerm = "Microsoft"
url = 'http://www.corporatecritic.org/home.aspx'

driver = webdriver.Chrome('./chromedriver')
driver.get(url)

searchBox = driver.find_element_by_id("txtSearch")
searchBox.send_keys(searchTerm)

submit = driver.find_element_by_id("btnSearch")
submit.click()

ethiScoreElement = driver.find_element_by_class_name("resultlistethiscore")
print(ethiScoreElement)


