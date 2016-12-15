# Readme
##### This repository houses Python scripts used to scrape the Boston Museum of Fine Arts collection. The scripts can be used scrape links to collection items after using the search feature on the BFMA website. The part of the collection I focused on was their extensive Tsuba, or sword hand gaurd, collection. The different folders denote steps in the process with "scrape links" being the first step.
##### Unfortunately the BFMA website doesn’t have a publicly available API so scraping the HTML code using the Python module BeautifulSoup was the easiest way to get the information within each item in the cataloge. Below will attempt to explain the rationale within each folder.

####"scraping links"
#####"titles1page.py" prints the links on the first page of results after one searches the collection on the BMFA website. "bmfabeautifulsoup2.py" scrapes the links from all the pages of a search result, if you search "Tsuba" in Arms and Armor. Since the results are 200 pages we need to tell python to insert the page number, up to 200, into the url while it loops. The links were in a "div" container on the search results page. "search-results-bmfa2.json"is the result of the previous script. This JSON will be used for the next step.

####"scrape inside the links"
#####"searchjson.py" loops through the resulting JSON line by line. The script tells python to go into the link, go to second and third div class called grid 6, and write that information to a new JSON. In order to strip the text of the HTML tags we need to try to match similar tags in order to drop them. Once we format the information into a list we take items in that list and name them for the JSON. Then write to JSON. In the top level directory there is a python script which will convert the JSON into a .csv with headers.


## Python Modules Needed
1. Beautiful Soup<br>
   <a href="https://www.crummy.com/software/BeautifulSoup/"> Documentation and Download</a>
2. Requests
3. JSON
4. CSV
