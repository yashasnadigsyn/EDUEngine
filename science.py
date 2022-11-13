import requests
from bs4 import BeautifulSoup as BS
import lxml, os, time

def runscience(query):
    URL = f"http://searx.thegpm.org/?q={query}&categories=science&language=en-US"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    r = requests.get(URL, headers=headers)
    soup = BS(r.content, 'lxml')
    main_results = soup.find_all("div", attrs={"class":"result"})
    title = []
    desc = []
    link = []
    datetime = []
    for i in main_results:
        try:
            title.append(i.h4.text)
        except:
            title.append("")
        try:
            desc.append(i.p.text)
        except:
            desc.append("No desc availible")
        try:
            external_link = i.find("div", attrs={"class":"external-link"})
            link.append(external_link)
        except:
            link.append("")
        try:
            datetime.append(i.time.text)
        except:
            datetime.append("No date availible")
    answer = []
    for i in range(len(title)):
        answerdict = {}
        answerdict['title'] = title[i]
        answerdict['desc'] = desc[i]
        answerdict['link'] = link[i].text
        answerdict['date'] = datetime[i]
        answer.append(answerdict)
    return answer