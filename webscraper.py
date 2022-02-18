import requests
from bs4 import BeautifulSoup

def scrapeReleasePage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    releaseHeaders = soup.find("div", {"class" : "repository-content"}).find_all("a", class_="Link--primary")
    currentRelease = releaseHeaders[0].text
    return currentRelease

def sendMessage(URL):
    versionHeader = scrapeReleasePage(url=URL)
    return versionHeader