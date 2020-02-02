import mechanize
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
import requests
import csv
import pandas as pd
import time

corporate_critic_url = "http://www.corporatecritic.org/companies.aspx"
amazon_url = 'https://www.amazon.ca/Nike-Black-Light-Brown-Basketball/dp/B077K81QDB/ref=sr_1_3?dchild=1&keywords=kobes&qid=1580603213&sr=8-3'


def find_company(url):
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')
    # keyword bylineinfo
    try:
        compName = soup.find(id="bylineInfo").text
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
    except:
        ethicsScore = -1

    return ethicsScore
filename = 'Extension/passData.csv'

company_name = find_company(amazon_url)
print(company_name+ ": ")
score = corporate_critic(company_name)
print("\t" + score)



