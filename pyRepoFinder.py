# pyRepoFinder 1.0;
# This script allows you to get a list of repositories related to a certain language and given search query.;
# Author : @vishalx360;
import random
import dateutil.parser
import requests

baseUrl = "https://api.github.com/"

# actual search web-api
# https://api.github.com/search/repositories?q=stars:>100+pushed:>2019-01-01+followers:>10+language:java


language_list = [
    "ActionScript",
    "C",
    "C#",
    "C++",
    "Clojure",
    "CoffeeScript",
    "CSS",
    "Go",
    "Haskell",
    "HTML",
    "Java",
    "JavaScript",
    "Lua",
    "MATLAB",
    "Objective-C",
    "Perl",
    "PHP",
    "Python",
    "R",
    "Ruby",
    "Scala",
    "Shell",
    "Swift",
    "TeX",
    "Vim script"
]
hashSeperator = "#############################"
# intro section
print("\n")
print(hashSeperator)
print("----# pyRepoFinder 1.0 #----- ")
print(hashSeperator)


# q=stars:>100+pushed:>2019-01-01+followers:>10+language:java
# defaults
query_stars = '>100'
query_lastUpdated = '>2019-01-01'
query_followers = '>10'
query_language = 'java'
query_search_keyword = 'web'


# START: language input section

# log
random_languages = ""
# logging random language
for i in range(4):
    random_languages += (random.choice(language_list) + ", ")

print("\n")
print("----~ Filter By Language ~----- \n")
print("""
 ! Popular Languages :-
     - %s
 
 ! Default : Java""" % random_languages)
print("\n")
# log

# getting input for language
inputLanguage = str(
    input(">>> Which Language do you want to filter by ? : ") or "Java")
query_language = inputLanguage
# END: language input section

# START: Search keyword section
# log
print("\n")
print("----~ Search-keywords ~-----")
print("""
 ! Search-keywords helps to filter repositories
   that contains given keyword in their name.
   for example :- Crypto

 ! Default : \"web\" 
    """)
# log
# getting input for query
inputKeyword = str(input(">>> Repo-Name must contain ? : ")
                   or query_search_keyword)
query_search_keyword = inputKeyword
print("\n")
# END: Search keyword section


# outputFileName input section
print("----~ Output File name ~-----")
print("""
 Specify Name of Output file
 
 ! If file already exists it will be overwritten.
 ! Only type name of file
 
 Default : output.txt

    """)
# getting input for outputFile name
outputFile = str(
    input(">>> What will be the name of output (.txt) file ? : ") or "output")


# payload
queryString = ('stars:%s+pushed:%s+followers:%s+language:%s %s' % (
    query_stars,
    query_lastUpdated,
    query_followers,
    query_language,
    query_search_keyword
))


# loging
print("\n")
print("Requesting Github API with provided parameters..... ")
print("\n")

# requesting
searchRepo = requests.get(
    (baseUrl + "search/repositories?per_page=100&q=" + queryString), timeout=10)

# converting to JSON
repoList = searchRepo.json()

# Writing header in output file
headerText = open((outputFile + '.txt'), 'w')
headerText.write("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pyRepoFinder 1.0;
Output for folowing parameters:-

- Main-language : %s
- Star-count : %s
- Followers-count : %s
- Last-commit by Date Range : %s
- Search parameter (Optional) : %s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
"""
                 % (
                     query_language,
                     query_stars,
                     query_followers,
                     query_lastUpdated,
                     query_search_keyword)
                 )
headerText.close()


# counter
counter = 1
# main loop
print("Writing to " + (outputFile + '.txt'))
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
print("Found %d Repositories  and saved in %s" %
      ((counter - 1), (outputFile + '.txt\n')))
