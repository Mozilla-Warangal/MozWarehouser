import json
from pprint import pprint
json_data=open('test.json')

data = json.load(json_data)
with open('List.txt', 'wb') as output:
	for x in range(1,30):
		pprint(data[x]['full_name'])
		output.write(data[x]['full_name']+'\n')

json_data.close()