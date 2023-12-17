import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com/'
r = requests.get(url)

#print(r)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class':'post-title'})

#print(title)

for t in title:
    print(t.getText())