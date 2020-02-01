import mechanize
from bs4 import BeautifulSoup

url = "http://www.corporatecritic.org/companies.aspx"
companyName = "nike"


def findEthicsScore(companyName):
    br = mechanize.Browser()
    br.open(url)
    br.select_form('Form1')
    br['txtSearch'] = companyName
    br.submit()
    soup = BeautifulSoup(br.response().read(), 'html.parser')
    ethicsScore = soup.select_one(".resultlistethiscore").text
    ethicsScore.strip('\n')
    ethicsScore.strip(' ')
    ethicsScore.strip('\t')
    print(ethicsScore)

    return ethicsScore

findEthicsScore(companyName)