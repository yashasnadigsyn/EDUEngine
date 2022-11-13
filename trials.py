import requests
from bs4 import BeautifulSoup as BS
import lxml

URL = "https://searx.be/search?q=googletrans%20nonetype%20site%3Astackoverflow.com&categories=general&language=en-US"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
r = requests.get(URL, headers=headers)
soup = BS(r.content, 'lxml')
main_results = soup.find_all("div", attrs={"class":"result"})
title = []
desc = []
link = []
for i in main_results:
    try:
        title.append(i.h4.text)
    except:
        title.append("")
    try:
        desc.append(i.p.text)
    except:
        desc.append("")
    try:
        external_link = i.find("div", attrs={"class":"external-link"})
        link.append(external_link.text)
    except:
        link.append("")
answer = []
for i in range(len(title)):
    answerdict = {}
    answerdict['title'] = title[i]
    answerdict['desc'] = desc[i]
    answerdict['link'] = link[i]
    answer.append(answerdict)

print(answer)