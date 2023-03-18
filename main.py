import requests
from bs4 import BeautifulSoup

URL = 'https://www.linkedin.com/jobs/search?keywords=&location=ireland&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("h3",class_="base-search-card__title")

for result in results:
    print(result)