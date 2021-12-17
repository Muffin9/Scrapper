import requests
from bs4 import BeautifulSoup


def extract_job(html):
    title = html.find('h2', {"itemprop": "title"})
    title = title.get_text(strip=True)
    company = html.find('span', {"itemprop": "hiringOrganization"}).find('h3', {"itemprop": "name"})
    company = company.get_text(strip=True)
    job_id = html['data-id']
    return {'title': title, 'company': company, 'link': f"https://remoteok.com/l/{job_id}"}


def extract_jobs(url):
    jobs = []
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                            'Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all('tr', {"class": 'job'})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://remoteok.com/remote-{word}-jobs"
    jobs = extract_jobs(url)
    return jobs
