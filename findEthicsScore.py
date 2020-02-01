import mechanize
from bs4 import BeautifulSoup

url = "http://www.corporatecritic.org/companies.aspx"
companyName = "nike"

br = mechanize.Browser()
br.open(url)
br.select_form('Form1')
br['txtSearch'] = companyName
br.submit()
soup = BeautifulSoup(br.response().read(), 'html.parser')
ethicsScore = soup.select_one(".resultlistethiscore").text

print(ethicsScore)

