# linkedin-job-scraper
Automated scraping tool for extracting job market data from linkedin


# Tools Used 

- Python 
  - Beautiful Soup


# Challenges faced
1. LinkedIn is not a static website and dynamically adds more job listings as you scroll down, this means you will only be able to see 25 listings when you request.
2. The URL for the job searches requires a GEOID that is not publically available so you basically build a script for each area you are searching
