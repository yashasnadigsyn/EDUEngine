import requests
from bs4 import BeautifulSoup as BS
import lxml

def runvideos(query):
    query = query.strip()
    query = query.replace(" ", "+")
    URL = f"https://yewtu.be/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    r = requests.get(URL, headers=headers)
    soup = BS(r.content, "lxml")
    main_posts = soup.find_all("div", attrs={"class":"pure-u-md-1-4"})
    answer = []
    for i in main_posts:
        try:
            thumbnail = i.img['src']
        except:
            thumbnail = 'https://community.atlassian.com/t5/image/serverpage/image-id/169924i0E4B9A8423A3B9CD/image-size/large?v=v2&px=999'
        try:
            duration = i.p.text
        except:
            duration = 'No data'
        try:
            link = i.a['href']
        except:
            link = "https://www.youtube.com/"
        try:
            title = i.find("p", attrs={"dir":"auto"})
        except:
            title = ''
        try:
            flex_left = i.find_all("div", attrs={"class":"flex-left"})
            author_name, author_link, date_uploaded = flex_left[0].find("p", attrs={"class":"channel-name"}).text, flex_left[0].a['href'], flex_left[1].p.text
        except:
            author_link, author_name, date_uploaded = 'No data', 'No data', 'No data'
        answers = {}
        answers['thumbnail'] = f"https://yewtu.be{thumbnail}"
        answers['duration'] = duration
        answers['link'] = f"https://yewtu.be{link}"
        answers['title'] = title.text
        answers['author_name'] = author_name
        answers['author_link'] = f"https://yewtu.be{author_link}"
        answers['date_uploaded'] = date_uploaded
        answer.append(answers)
    return answer