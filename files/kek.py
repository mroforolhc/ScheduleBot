import requests
import json

groups = {}
fac = ['26', '5', '11', '152', '12', '164', '157', '7', '154', '289', '167', '124', '163', '150', '153', '159', '2']

for i in range(len(fac)):
	for j in range(6):
		url = 'http://oreluniver.ru/schedule/{}/{}/grouplist'.format(fac[i], j)
		r = json.loads(requests.get(url).text)
		for z in range(len(r)):
			groups[r[z]['title']] = r[z]['idgruop']

print(groups)

