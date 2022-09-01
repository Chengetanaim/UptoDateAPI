from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url = "https://ihararejobs.com/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
jobs = page_soup.findAll("div", {"class": "listings job"})
job_links = []
company_names = []
descriptions = []
job_types = []
dates_added = []
for job in jobs:
    job_link = "https://ihararejobs.com" + job.a["href"]
    company_name = job.div.h3.span.strong.text
    description = job.div.h3.a["title"]
    containers = job.div.findAll("span", {"class": "date"})
    for container in containers:
        job_type = container.small.text
        elements = container.text
        elements2 = " ".join(elements.split())
        list_elements = elements2.split()
        date_added = list_elements[2] + " " + list_elements[3] + " " + list_elements[4]
    
    job_links.append(job_link)
    company_names.append(company_name)
    descriptions.append(description)
    job_types.append(job_type)
    dates_added.append(date_added)
    


    # print(job_link)
    # print(company_name)
    # print(description)
    # print(job_type)
    # print(date_added)
    # print("")
