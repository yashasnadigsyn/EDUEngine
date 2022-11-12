from libgen_api import LibgenSearch
import requests
from bs4 import BeautifulSoup as BS
import lxml

libgen = LibgenSearch()
results = libgen.search_title("head first python")
for i in results:
    try:
        Title = i['Title']
    except:
        Title = ''
    try:
        Author = i['Author']
    except:
        Author = ''
    try:
        Year = i['Year']
    except:
        Year = ''
    try:
        Pages = i['Pages']
    except:
        Pages = ''
    try:
        Language = i['Language']
    except:
        Language = ''
    try:
        Size = i['Size']
    except:
        Size = ''
    try:
        Mirror_1 = i['Mirror_1']
    except:
        Mirror_1 = ''
    try:
        Mirror_2 = i['Mirror_2']
    except:
        Mirror_2 = ''
    try:
        Mirror_3 = i['Mirror_3']
    except:
        Mirror_3 = ''
    try:
        Mirror_4 = i['Mirror_4']
    except:
        Mirror_4 = ''
    r = requests.get(Mirror_1)
    soup = BS(r.content, 'lxml')
    allinks = soup.find_all('a')
    for j in allinks:
        if 'IPFS' in j.text:
            Direct_Link = j['href']

    print(f"""
    Title: {Title}
    Author: {Author}
    Year: {Year}
    Pages: {Pages}
    Language: {Language}
    Size: {Size}
    Mirror 1: {Mirror_1}
    Mirror 2: {Mirror_2}
    Mirror 3: {Mirror_3}
    Mirror 4: {Mirror_4}
    Direct Link: {Direct_Link}
    """)

    

