import mechanize
from bs4 import BeautifulSoup
import re

url = "http://www.corporatecritic.org/companies.aspx"
companyName = "amazon"


def findEthicsScore(companyName):
    br = mechanize.Browser()
    br.open(url)
    br.select_form('Form1')
    br['txtSearch'] = companyName
    br.submit()
    try:
        soup = BeautifulSoup(br.response().read(), 'html.parser')
        ethicsScore = soup.select_one(".resultlistethiscore").text
        ethicsScore = re.sub(' ', '', ethicsScore)
        ethicsScore = re.sub(chr(13), '', ethicsScore)
        ethicsScore = re.sub(chr(10), '', ethicsScore)
        ethicsScore = re.sub('\)', '', ethicsScore)
        ethicsScore = re.sub('\(', '', ethicsScore)
        #print(ethicsScore)
    except:
        ethicsScore = -1
        #print(ethicsScore)

    return ethicsScore


findEthicsScore(companyName)
