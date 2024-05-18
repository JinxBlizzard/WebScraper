from bs4 import BeautifulSoup
import requests
import time

anti_filter = input(">")
print(f"Removing Skills : {anti_filter}")


def job_filter():
    html_text = requests.get(
        'https://internshala.com/internships/keywords-python/?utm_source=hp_internship_keyword_search').text

    soup = BeautifulSoup(html_text, features="html.parser")
    jobs = soup.find_all('div', class_="internship_meta")

    for job in jobs:
        get_time = job.find('div', class_="status status-small status-success")
        # get_company_name = job.find('a', class_="link_display_like_text")
        get_job_type = job.find('div', class_="company")
        if get_time is not None:
            get_job_type = get_job_type.text.replace('\n', '')
            get_job_type = get_job_type.replace(' ', '')
            get_time = get_time.text.replace('\n', '')
            print(f"""
            job type = {get_job_type}
            time posted = {get_time.strip()}
            """)


if __name__ == "__main__":
    while True:
        job_filter()
        time.sleep(600)
