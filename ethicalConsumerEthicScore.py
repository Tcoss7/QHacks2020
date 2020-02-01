import mechanize
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
import requests

url = "https://guide.ethical.org.au/guide/search/"
companyName = "Nestle"

br = mechanize.Browser()
br.set_handle_robots(False)
br.open(url)
br.select_form(id="searchform")
br['term'] = companyName
br.submit()

soup = BeautifulSoup(br.response().read(), 'lxml')
table = soup.find('td', attrs={'class':'tdformData'})
company_url = table.find('a', href=True)['href']
print(company_url)
source = requests.get(company_url)

# print(soup.prettify())
# soup = BeautifulSoup(source, 'lxml')
# ethicsScore = soup.find('div', attrs={'sytle':'float:right; margin:0px 0px 20px 20px;'})
# print(ethicsScore)

