import mechanize
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
import requests
import csv
import pandas as pd
import time

corporate_critic_url = "http://www.corporatecritic.org/companies.aspx"


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
        print(ethicsScore)
    except:
        ethicsScore = -1

    return ethicsScore
filename = 'Extension/passData.csv'

while True:
	time.sleep(2)
	try:
		df = pd.read_csv(filename)
		product_url = ''
		for entry in df:
			product_url+=entry
		final_ethics_score = corporate_critic(find_company(product_url))
		
		f = open(filename, "w+")
		f.close()
	except:
		print("lol")


	

#final_ethics_score = corporate_critic(find_company(product_url))
#print(final_ethics_score
