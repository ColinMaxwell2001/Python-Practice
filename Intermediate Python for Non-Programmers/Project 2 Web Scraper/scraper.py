import requests
from bs4 import BeautifulSoup
import datetime

url = "https://pixelford.com/blog/"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article', class_="type-post") #Finds all article tags within the website

for blog in blogs: #for all article tags with class="type-post"
    title = blog.find('a', class_="entry-title-link").get_text()
    
    blog_datetime_string = blog.find('time', class_="entry-time").get('datetime')
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date = blog_datetime.strftime("%A %b %m %H ")
    print(f"{pretty_date} - {title}")