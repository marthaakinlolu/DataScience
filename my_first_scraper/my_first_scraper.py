import requests
from bs4 import BeautifulSoup
import csv
url = "https://github.com/trending"

def request_github_trending(url):
    response = requests.get(url)
    return response

def extract(page):
    page_soup = BeautifulSoup(page.content, "html.parser")
    # pg_soup = page_soup.prettify()
    find_all = page_soup.find('article', attrs = {'class': 'Box-row'})
    repos = page_soup.find_all("h1", class_="h3 lh-condensed")
    return repos

def transform(html_repos):
    repo = []
    for row in html_repos:
        developer = row.find("span", class_ ="text-normal")
        repo_name = row.find("a")
        nbr_stars = row.find("a", class_="muted-link")
        repo.append({'developer': developer, 'repository_name': repo_name, 'nbr_stars': nbr_stars})
    return repo


def format(repositories_data):
    data_csv = "Repositories Data\n"
    for row in repositories_data:
        data_csv += f"{row['developer']},{row['repository_name']},{row['nbr_stars']}\n"
    return data_csv