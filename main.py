from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

browser.get(f"{base_url}{search_term}")

response = browser.page_source

job_DB = []

soup = BeautifulSoup(response,"html.parser")
job_list = soup.find("ul",class_="css-zu9cdh eu4oa1w0")
jobs = job_list.find_all("li",class_="css-5lfssm eu4oa1w0",recursive="False")

for job in jobs:
    zone = job.find("div",class_="mosaic-zone")
    if zone == None :
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.select_one(".company_location div span").string
        location = job.select_one(".company_location div div").string
        job_data = {
            'link' : f"https://kr.indeed.com{link}",
            'company' : company,
            'location' : location,
            'position' : title,
        }
        job_DB.append(job_data)
        
for result in job_DB:
    print(result, "\n////////\n")