
from bs4 import BeautifulSoup
 
#we also want to have a way to talk to the internet so we need the request module too
import requests, json

all_urls = []
current_page = 0
while current_page <= 199:

	url = "http://www.mfa.org/collections/search?search_api_views_fulltext=tsuba&page=" + str(current_page) + "&f[0]=field_classifications%3A152"

	current_page = current_page + 1
	print("Downloading Page" + str(current_page))
	search_page = requests.get(url)
	page_html = search_page.text

	soup = BeautifulSoup(page_html, "html.parser")

	divs = soup.find_all("div", attrs = {"class":"flex-caption"})

	for links in divs:

		a = links.find("a")
		all_urls.append(a['href'])

		##to test results
		#print(json.dumps(all_urls,indent=4))
		
with open('search-results-bmfa2.json', 'w') as f:
	f.write(json.dumps(all_urls,indent=4))
    
		#print(a['href'])