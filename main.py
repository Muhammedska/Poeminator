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
lux = []

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

        os.system('cls' if os.name == 'nt' else 'clear')
        founded += 1
    for m in PoemLinks:
        url = m
        r = requests.get(url, verify=False)
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find('pre', attrs={'class': 'stext'})
        try:
            PoemGenie.append(table.text)
            lux.append(table.text)
        except AttributeError:
            pass
    allPoem.append([url.replace("http://siir.me/",''),PoemGenie])
    print(len(allPoem),' all the poem ')
file = open('poems.txt','w',encoding='UTF-8')
for i in lux:
    print(i.encode('utf-8'))
    file.write(i)
