import requests
from bs4 import BeautifulSoup

URL = 'https://www.linkedin.com/jobs/search?keywords=Data%20Engineer&location=Ireland&geoId=104738515&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=2'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('ul', class_='jobs-search__results-list')
results = results.find_all('li')
job_listings = []

for result in results:
    try:
        job_id = result.find('div')
        job_id = job_id.get('data-entity-urn').split(':')[-1]
        job_title = result.find('h3', class_="base-search-card__title")
        job_recruiter = result.find('a', class_="hidden-nested-link")
        job_location = result.find('span', class_="job-search-card__location")
        job_title = job_title.contents[0].strip()
        job_recruiter = job_recruiter.contents[0].strip()
        job_location = job_location.contents[0].strip()
        job_listings.append({'id':job_id, "title": job_title, "recruiter": job_recruiter, "location": job_location})

    except Exception as e:
        print(e)
        continue


for job in job_listings:
    print(job)