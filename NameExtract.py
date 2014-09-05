import json
from pprint import pprint
import os

def count_files(in_directory):
    joiner= (in_directory + os.path.sep).__add__
    return sum(
        os.path.isfile(filename)
        for filename
        in map(joiner, os.listdir(in_directory))
    )

totalfiles_in_dir=count_files("CodeBase/");
with open('List.txt', 'wb') as output:
	for pagenumber in range(1,totalfiles_in_dir):
		json_data=open('CodeBase/repos?page='+str(pagenumber))
		data = json.load(json_data)
		for x in range(1,30):
			pprint(data[x]['full_name'])
			output.write(data[x]['full_name']+'\n')

json_data.close()