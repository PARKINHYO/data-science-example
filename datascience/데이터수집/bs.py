from bs4 import BeautifulSoup
import requests
import urllib3

url = ("http://www.kpu.ac.kr/front/boardview.do?pkid=87620&currentPage=1&searchField=ALL&siteGubun=1&menuGubun=1&bbsConfigFK=1&searchLowItem=ALL&searchValue=")
html = requests.get(url).text

soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.findAll('span')
print(first_paragraph)


