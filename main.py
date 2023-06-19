# imports
from bs4 import BeautifulSoup
import requests
import csv

# Site url
URL = 'https://www.cv-library.co.uk/junior-python-developer-jobs'

# Get request
response = requests.get(URL)
website_html = response.text

# BeautifulSoap object
soap = BeautifulSoup(website_html, 'html.parser')

# finding data using tags and classes
all_job_names = soap.find_all(name="h2", class_='job__title')
all_company_name = soap.find_all(name='a', class_='job__company-link')
all_locations = soap.find_all(name='span', class_='job__details-location')
all_salary = soap.find_all(name='dd', class_='job__details-value salary')

# extract text from each data
job_names = [job.getText() for job in all_job_names]
company_names = [name.getText() for name in all_company_name]
locations = [loc.getText() for loc in all_locations]
all_salary = [salary.getText() for salary in all_salary]

# write data into csv file
with open("Jobs.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(job_names)
    writer.writerow(company_names)
    writer.writerow(locations)
    writer.writerow(all_salary)
