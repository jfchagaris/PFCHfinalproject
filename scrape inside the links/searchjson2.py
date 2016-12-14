import json, requests, re
from bs4 import BeautifulSoup

with open('search-results-bmfa2.json', 'r') as f:
	tsubadata = []
	urls = json.load(f)

	imgregex = re.compile('http.*\.jpg')

	for link in urls:


			print(link)

			print("Downloading Page" + (link))
			search_page = requests.get(link)
			page_html = search_page.text

			soup = BeautifulSoup(page_html, "html.parser")
			imgdiv = soup.find("div", attrs = {"class":"image"})
			divs = soup.find_all("div", attrs = {"class":"grid-6"})
			left_side = divs[2]
			right_side = divs[3]
			imgstring = str(imgdiv)
			imglink = imgregex.findall(imgstring)
			title = left_side.find('h2').text
			period = []
			nice_period = str(left_side.find('p'))
			nice_period = nice_period.replace('<br>', '</br>')
			nice_period = nice_period.replace('<p>', '')
			nice_period = nice_period.replace('</p>','')
			nice_period = nice_period.split('</br>')
			period.append(nice_period)

			data = {}

			data['URL'] = link
			data['title'] = title
			data['country'] = nice_period[0]
			data['dynastic period'] = nice_period[1]
			data['time period'] = nice_period[2]
			data['image'] = imglink
			tsubadata.append(data)

with open('tsubadata.json', 'w') as d:
		d.write(json.dumps(tsubadata,indent=4))
