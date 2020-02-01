from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests

url = 'https://www.amazon.ca/dp/B07L3R93F2?aaxitk=xL8buRWZjNlIiQISzOBT2A&pd_rd_i=B07L3R93F2&pf_rd_p=aa0a7a36-9d2d-49bd-b59d-ceef667a2a55&hsa_cr_id=6969753180801&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F81lQp%2BbmaSL.jpg&sb-ci-a=B07L3R93F2'

source = requests.get(url).text


soup = BeautifulSoup(source, 'lxml')
#keyword bylineinfo
try:
	compName = soup.find(id="bylineInfo").text
	print(soup.prettify)
except:
	print("exception code")
	session = HTMLSession()
	resp = session.get(url)
	resp.html.render()
	source = resp.html.html
	soup = BeautifulSoup(source, 'lxml')
	compName = soup.find(id="bylineInfo").text
	print(compName)
