# importing
import requests
from bs4 import BeautifulSoup
print("\n\n#########################################\n\n")

repoHref = "/vishalx360/vishalx360.github.io"
baseURL = "https://github.com"

# requesting
data = requests.get(baseURL + repoHref)

# parsing
soup = BeautifulSoup(data.text, 'html.parser')


# * repo Total number of commits
# repoTotalCommits
repoTotalCommits = soup.find('li', {'class': 'commits'}).find(
    'span', {'class': "num text-emphasized"}).text.strip()


CommitContainer = soup.find_all('td', {'class': 'message'})[0].find('a')

# * last commit text
lastCommit = CommitContainer.text.strip()

# * last commit URL
lastCommitURl = (baseURL + CommitContainer['href'])

# # * last commit date
lastCommitDate = soup.find_all('td', {'class': 'age'})[
    0].find('time-ago').text.strip()

# lastCommitDateTime = lastCommitLi.find('relative-time')


commitDetails = {
    'totalCommits': repoTotalCommits,
    'lastCommit': lastCommit,
    'lastCommitURL': lastCommitURl,
    'lastCommitDate': lastCommitDate
}

print(commitDetails)
