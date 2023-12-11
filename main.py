from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
#코드를 중간에 멈추게 하기 위해

p = sync_playwright().start()

browser = p.chromium.launch()
#chromium 대신 firefox, safari등 가능

page = browser.new_page()
#새탭 열기

page.goto("https://www.wanted.co.kr/search?query=flutter")

time.sleep(3)

# page.click("button.Aside_searchButton__Xhqq3")

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

page.click("a#search_tab_position")

time.sleep(2)

for x in range(5) :
    page.keyboard.down("End")
    time.sleep(2)

content = page.content()

time.sleep(3)
p.stop()

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

print(jobs_db)    
print(len(jobs_db))