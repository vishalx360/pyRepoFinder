# importing
import sys
import requests
from bs4 import BeautifulSoup


def getCommitDetails(url):
    class commitDetails:
        def __init__(self, repoTotalCommits, lastCommit, lastCommitURl, lastCommitISODate, lastCommitDate):
            self.totalCommits = repoTotalCommits,
            self.lastCommit = lastCommit,
            self.lastCommitURL = lastCommitURl,
            self.lastCommitISODate = lastCommitISODate
            self.lastCommitDate = lastCommitDate

    # requesting
    data = requests.get(url)
    # parsing
    soup = BeautifulSoup(data.text, 'html.parser')

    # * repo Total number of commits
    # repoTotalCommits
    repoTotalCommits = soup.find('li', {'class': 'commits'}).find(
        'span', {'class': "num text-emphasized"}).text.strip()

    CommitContainer = soup.find_all('td', {'class': 'message'})[0].find('a')

    # * last commit text
    try:
        lastCommit = CommitContainer.text.strip()
    except AttributeError:
        print("API Error, try after some time")
        sys.exit(0)
    # * last commit URL
    lastCommitURl = (CommitContainer['href'])

    # # * last commit date
    lastCommitISODate = soup.find_all('td', {'class': 'age'})[
        0].find('time-ago')['datetime']

    lastCommitDate = soup.find_all('td', {'class': 'age'})[
        0].find('time-ago').text.strip()

    newDetail = commitDetails(
        repoTotalCommits, lastCommit, lastCommitURl, lastCommitISODate, lastCommitDate)
    return newDetail


# x = getCommitDetails("https://github.com/cSploit/android")

# x.lastCommitISODate

# print(x.lastCommitISODate)
