from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv
#comma seperated values
#mac os , exel 등 다양한 프로그램에 범용적이다.

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
#chromium 대신 firefox, safari등 가능
page = browser.new_page()
#새탭 열기

key = "flutter"
page.goto("https://www.wanted.co.kr/search?query={key}&tab=position")

for x in range(5) :
    page.keyboard.down("End")
    time.sleep(2)

content = page.content()
time.sleep(3)
p.stop()

#정보 다 불러왔음

soup = BeautifulSoup(content, "html.parser")

jobs_db = []

jobs = soup.find_all("div",class_="JobCard_container__FqChn JobCard_container--variant-card__znjV9")

for job in jobs :
    link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
    title = job.find("strong",class_="JobCard_title__ddkwM").text
    company_name = job.find("span",class_="JobCard_companyName__vZMqJ").text
    location = job.find("span",class_="JobCard_location__2EOr5").text
    reward = job.find("span",class_="JobCard_reward__sdyHn").text
    job = {
        "link":link ,
        "title":title ,
        "company_name":company_name ,
        "location":location ,
        "reward": reward
    }
    jobs_db.append(job)
     
print(len(jobs_db))

file = open("jobs.csv","w")
writer = csv.writer(file)
#row는 행이다
#행은 리스트를 받는다. 딕셔너리는 안된다. 이떄 쓰는 함수가 딕셔너리.values() // 딕셔너리.kets()
writer.writerow(["Title","Comapany","Location","Reward","Link"])

for job in jobs_db :
    writer.writerow(job.values())

file.close()