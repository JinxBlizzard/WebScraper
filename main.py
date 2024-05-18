from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://internshala.com/internships/keywords-python/?utm_source=hp_internship_keyword_search').text

soup = BeautifulSoup(html_text, features="html.parser")
jobs = soup.find_all('div', class_="internship_meta")

for job in jobs:
    get_time = job.find('div', class_="status status-small status-success")
    get_company_name = job.find('a', class_="link_display_like_text")
    get_job_type = job.find('div', class_="company")
    if get_company_name is not None:
        get_job_type = get_job_type.text.replace(' \n', '')
        get_time = get_time.text.replace(' \n', '')
        print(f"""
        company name = {get_company_name.text}
        job type = {get_job_type}
        time posted = {get_time}
        """)
    # get_name = job.find('i', class_="ic-16-reschedule")
# <div class="status status-small status-info"><i class="ic-16-reschedule"></i>7 days ago</div>

