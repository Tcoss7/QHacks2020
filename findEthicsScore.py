import mechanize
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
import requests

corporate_critic_url = "http://www.corporatecritic.org/companies.aspx"
product_url = 'https://www.amazon.ca/dp/B07L3R93F2?aaxitk=xL8buRWZjNlIiQISzOBT2A&pd_rd_i=B07L3R93F2&pf_rd_p=aa0a7a36-9d2d-49bd-b59d-ceef667a2a55&hsa_cr_id=6969753180801&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F81lQp%2BbmaSL.jpg&sb-ci-a=B07L3R93F2'


def find_company(url):
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')
    # keyword bylineinfo
    try:
        compName = soup.find(id="bylineInfo").text
        print(soup.prettify)
    except:
        #print("exception code")
        session = HTMLSession()
        resp = session.get(url)
        resp.html.render()
        source = resp.html.html
        soup = BeautifulSoup(source, 'lxml')
        compName = soup.find(id="bylineInfo").text
        print(compName)
    return compName


def corporate_critic(companyName):
    br = mechanize.Browser()
    br.open(corporate_critic_url)
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
        print(ethicsScore)
    except:
        ethicsScore = -1

    return ethicsScore


final_ethics_score = corporate_critic(find_company(product_url))
print(final_ethics_score)
