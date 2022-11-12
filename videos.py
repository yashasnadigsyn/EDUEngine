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
    for i in main_posts:
        thumbnail = i.img['src']
        duration = i.p.text
        link = i.a['href']
        title = i.find("p", attrs={"dir":"auto"})
        flex_left = i.find_all("div", attrs={"class":"flex-left"})
        author_name, author_link, date_uploaded = flex_left[0].find("p", attrs={"class":"channel-name"}), flex_left[0].a['href'], flex_left[1].p.text
        print(f"""
        Title: {title.text}
        Duration: {duration}
        Thumbnail: {thumbnail}
        Link: {link}
        Channel: {author_name}
        Channel_link: {author_link}
        date uploaded: {date_uploaded}
        """)


