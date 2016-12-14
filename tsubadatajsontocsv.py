import csv
import json

with open ('tsubadata.json','r') as f:
	with open ('tsubadata.csv','w') as d:
		
		x = json.load(f)

		b = csv.writer(d)

		b.writerow(["URL", "title", "country", "dynastic period", "time period", "image"])

		for arecord in x:
			b.writerow([arecord["URL"],
				arecord["title"],
				arecord["country"],
				arecord["dynastic period"],
				arecord["time period"],
				arecord["image"]])
		print(x)