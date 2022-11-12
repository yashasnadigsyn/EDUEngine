import requests
from bs4 import BeautifulSoup as BS
import lxml

query = input("query? ")
query = query.strip()
query = query.replace(" ", "+")
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
URL = "https://stackoverflow.com/search?q=googletrans+nonetype&s=qwundcid-edc-sdvffsv-dvfvfeabv"
print(URL)
r = requests.get(URL, headers=headers)
soup = BS(r.content, 'lxml')
posts = soup.find_all("div", attrs={"class":"js-post-summary"})
print(soup.prettify())
for i in posts:
    print(i.h3.text)
    try:
        answers = i.find("div", attrs={"class":"has-accepted-answer"})
        answers = answers.text.strip()
    except:
        answers = ""
    try:
        tags = i.find("div", attrs={"class":"js-tags"})
        tags = tags.text.strip()
    except:
        tags = ""
    print(f"{answers}\n{tags}\n")