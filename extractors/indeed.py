from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def get_page_count(keyword):
    browser = webdriver.Chrome(options=options)
    base_url = "https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    response = browser.page_source
    
    soup = BeautifulSoup(response,"html.parser")
    
    pagination = soup.select_one("nav ul")
    pages = pagination.find_all("li",recursive="False")
    count = len(pages)
    if count == 0 :
        return 0
    elif count >=5:
        return 5
    else:
        return count-1
    
def extract_indeed_jobs(keyword) :
    browser = webdriver.Chrome(options=options)
    pages = get_page_count(keyword)
    job_DB = []
    
    for page in range(pages) :
        base_url = "https://kr.indeed.com/jobs?q="
        browser.get(f"{base_url}{keyword}&start={page*10}")
        response = browser.page_source
        
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
                    'company' : company.replace(","," "),
                    'location' : location.replace(","," "),
                    'position' : title.replace(","," "),
                }
                job_DB.append(job_data)
    return job_DB