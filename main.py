import os

import requests
from bs4 import BeautifulSoup
import csv
import urllib3

urllib3.disable_warnings()



url = "http://siir.me/"
r = requests.get(url, verify=False)
soup = BeautifulSoup(r.content, "html.parser")

PoemLinks = []
PoetristList = []
allPoem = []

table = soup.find('ul', attrs={'class': 'isairler'})
founded = 1
for row in table.findAll('li'):
    PoetristList.append(row.a['href'])
    print('We Found {} Poetrist'.format(founded))
    os.system('cls' if os.name=='nt' else 'clear')
    founded += 1
founded = 1
for i in PoetristList:
    url = i
  
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content, "html.parser")

    PoemLinks = []
    PoemGenie = []
    table = soup.find('ul', attrs={'class': 'siirler'})
    founded = 1
    for row in table.findAll('li'):
        PoemLinks.append(row.a['href'])
        print('We Found {} Poem'.format(founded))
        os.system('cls' if os.name == 'nt' else 'clear')
        founded += 1
    for m in PoemLinks:
        url = m
        r = requests.get(url, verify=False)
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find('pre', attrs={'class': 'stext'})
        PoemGenie.append(table.text)
    allPoem.append([url.replace("http://siir.me/",''),PoemGenie])
for i in allPoem:
    print(i)
