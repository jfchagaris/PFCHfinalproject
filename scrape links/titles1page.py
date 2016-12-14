##This program prints the titles of the items of the collection page.
##The page is sorted by 'Asia' and 'Arms and Armor'. The goal is to get
##titles, artists, assession number and link for all pages. Another goal
##is to write to json, but only the entries with Tsuba in the name. 

import requests, json

all_art = []

url = "http://www.mfa.org/collections/search?f[0]=field_classifications%3A152&f[1]=field_collections%3A2"

painting_page = requests.get(url)
page_html = painting_page.text

soup = BeautifulSoup(page_html, "html.parser")

all_li = soup.find_all("h5")

div = soup.find("div", attrs = {"class":"flex-caption"})

##This prints the first enrty with the the artists, assession number,
## and date
#print(div.text)

for a_li in all_li:
 	print(a_li.text)