from libgen_api import LibgenSearch
import requests
from bs4 import BeautifulSoup as BS
import lxml

def runfiles(query):
    libgen = LibgenSearch()
    results = libgen.search_title(query)
    answer = []
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
            Language = i['Language']
        except:
            Language = ''
        try:
            Mirror_1 = i['Mirror_1']
        except:
            Mirror_1 = ''
        try:
            Mirror_2 = i['Mirror_2']
        except:
            Mirror_2 = ''
        r = requests.get(Mirror_1)
        soup = BS(r.content, 'lxml')
        allinks = soup.find_all('a')
        for j in allinks:
            if 'IPFS' in j.text:
                Direct_Link = j['href']
        answers = {}
        answers['Title'] = Title
        answers['Author'] = Author
        answers['Year'] = Year
        answers['Language'] = Language
        answers['Mirror_1'] = Mirror_1
        answers['Mirror_2'] = Mirror_2
        answers['Direct_Link'] = Direct_Link
        answer.append(answers)
    return answer
        


    

