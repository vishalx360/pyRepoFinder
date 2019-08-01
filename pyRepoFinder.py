# pyRepoFinder 1.0;
# This script allows you to get a list of repositories related to a certain language and given search query.;
# Author : @vishalx360;


import requests
import dateutil.parser

baseUrl = "https://api.github.com/"

# actual search web-api
# https://api.github.com/search?l=Java&q=java&type=Repositories


payload = {
    "q": "query",
    "l": "language",
    "type": 'Repositories'
}

# getting input for query
inputQuery = str(input("Type Input query : ") or "java")
payload['q'] = inputQuery

# getting input for language
inputLanguage = str(input("Type Language : ") or "Java")
payload['l'] = inputLanguage

# getting input for outputFile name
outputFile = str(input("Output txt file : ") or "output")


# requesting
print("\n")
print("Requesting Github API ..... ")

# accessing API
searchRepo = requests.get(
    (baseUrl + "search/repositories"), params=payload, timeout=5)


# converting to JSON
repoList = searchRepo.json()


# cleaning output file
tempOutputFile = open((outputFile + '.txt'), 'w')
tempOutputFile.write("")
tempOutputFile.close()


# counter
counter = 1

# main loop
for item in repoList['items']:
    if (item['stargazers_count'] > 100) & (item["watchers_count"] > 20):
        # using context-manager to open file.
        with open((outputFile + '.txt'), 'a+') as opened_file:
            # writing repo name.
            opened_file.write("%d. Repo Name: %s\n" %
                              (counter, item['name']))
            # writing repo url.
            opened_file.write("Repo URL: %s\n" % item['html_url'])
            # parsing ISO-8601 date.
            newDate = dateutil.parser.parse(item['updated_at']).date()
            opened_file.write("Last Event At: %s" % newDate)

            # adding spaces.
            opened_file.write("\n \n")
            # incrimenting counter.
            counter += 1


# logging details of request
print("Found %d Repositories and saved in %s" %
      ((counter - 1), (outputFile + '.txt')))
