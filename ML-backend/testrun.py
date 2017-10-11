import requests
import json
import pickle



def printjson(abctext):
	# print type(abctext)
	parsed = json.loads(abctext)
	print json.dumps(parsed,indent=4,sort_keys=True)

from get_sources import generate_maybe_sources_file,SOURCES_FILE_NAME

with open(SOURCES_FILE_NAME,'rb') as f :
	s_names = pickle.load(f) 

print s_names


def get_news(source):
	print source
	key = 'ae8904ae7a674eff8a83ae5e83da410f'
	r = requests.get('https://newsapi.org/v1/articles?source='+source+'&sortBy=latest&apiKey='+key)
	printjson(r.text)



get_news(s_names[1])
get_news(s_names[2])
get_news(s_names[3])