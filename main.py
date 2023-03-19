import requests
from bs4 import BeautifulSoup


def get_html_data(job_title: str, location: str):
    try:
        URL = 'https://www.linkedin.com/jobs/search?keywords=Data%20Engineer&location=Ireland&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
        html_data = requests.get(URL)

    except: 
        print("Could not access given URL")

    return html_data

def get_job_list_elements(html_data):
    try:
        html_soup_object = BeautifulSoup(html_data.content, "html.parser")
        job_list = html_soup_object.find('ul', class_='jobs-search__results-list')
        job_list_elements = job_list.find_all('li')
    
    except Exception as e:
        print("Could not extract elements from HTML data")
        print('Error:', e)

    return job_list_elements

def extract_jobs(job_elements):
    job_listings = []

    for job in job_elements:
        try:
            job_id = job.find('div')
            job_id = job_id.get('data-entity-urn').split(':')[-1]
            job_title = job.find('h3', class_="base-search-card__title")
            job_recruiter = job.find('a', class_="hidden-nested-link")
            job_location = job.find('span', class_="job-search-card__location")
            job_title = job_title.contents[0].strip()
            job_recruiter = job_recruiter.contents[0].strip()
            job_location = job_location.contents[0].strip()
            job_listings.append({'id': job_id, "title": job_title,
                                "recruiter": job_recruiter, "location": job_location})
        except Exception as e:
            print(e)
            continue
        
    return job_listings

def get_jobs(position: str, location: str):

    html_data = get_html_data(position, location)
    job_listings_elements = get_job_list_elements(html_data)
    job_dict = extract_jobs(job_listings_elements)
    for job in job_dict:
        print(job)


if __name__ == "__main__":
    get_jobs('Data Engineer', 'Ireland')