from bs4 import BeautifulSoup
import requests
import time

print("Put some skills you are unfamiliar with:")
unfamiliar_skill = input("")
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        date_published= job.find('span', class_= "sim-posted").text
        if 'few' in date_published:
            company_name = job.find('h3', class_ = "joblist-comp-name").text
            skills = job.find('div', class_ = "srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Skills Required: {skills.strip()}\n")
                    f.write(f'More Info: {more_info}')
                print(f"File Saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
