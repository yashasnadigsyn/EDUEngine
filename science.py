import requests
from bs4 import BeautifulSoup as BS
import lxml, os, time

query = "facenet tensorflow"
categ = "science"
r = requests.get(f"http://searx.thegpm.org/?q=rust%20book&categories=science&language=en-US")
soup = BS(r.content, 'lxml')
main_results = soup.find_all("div", attrs={"class":"result"})
for i in main_results:
    if i.h4:
        print(i.h4.text)
    if i.p:
        print(i.p.text)
    try:
        external_link = i.find("div", attrs={"class":"external-link"})
        print(external_link.text)
    except:
        print("")
    if i.time:
        print(i.time.text)
    print("\n\n-----------------------------------------------------------------------------\n\n")