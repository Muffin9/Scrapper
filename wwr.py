import requests
from bs4 import BeautifulSoup


def extract_job(html):
    title = html.find("span", {"class": "title"}).string
    company = html.find("span", {"class": "company"}).string
    for tag in html.find_all('div', {"class": "tooltip"}):
        tag.extract()

    job_id = html.find("a")['href']
    return {'title': title, 'company': company, 'link': f"https://weworkremotely.com{job_id}"}


def extract_jobs(url):
    jobs = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("li", {"class": "feature"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={word}"
    jobs = extract_jobs(url)
    return jobs
