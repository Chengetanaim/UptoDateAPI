from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://news.yahoo.com/us/'
uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("h3", {"class": "Mb(5px)"})
titles = []
website_links = []
for container in containers:
    title = container.a.text
    website_link = "https://news.yahoo.com" + container.a["href"]
    titles.append(title)
    website_links.append(website_link)    