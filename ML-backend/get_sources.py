import requests
import pickle 
import os

SOURCES_FILE_NAME = 'sources.sc'

def generate_maybe_sources_file():

	# check for SOURCES_FILE_NAME
	sourcesFilePresent = False 
	cur_dir = os.getcwd()
	file_list = os.listdir(cur_dir)
	if SOURCES_FILE_NAME in file_list :
		sourcesFilePresent = True
	if sourcesFilePresent is False :
		print 'Creating Sources File.'
		save_sources(logs =True)
	else :
		print 'File Exists.'


def save_sources(logs = False):
	if logs is True :
		print 'Establishing Connection...'
	try :
		sjson = requests.get('https://newsapi.org/v1/sources?language=en').json()
	except :
		print 'No internet Connection'
		exit()

	if sjson['status'] != 'ok' :
		print 'Unable to Connect'
		exit()

	# becomes a list.
	sjson = sjson['sources']

	if logs is True :
		print 'Creating List of Names...',

	names = []
	for source in sjson :
		name = source['name']
		name = '-'.join([x.lower() for x in name.split(' ')])
		names.append(name)
	if logs is True :
		print 'Saving Names'
	with open(SOURCES_FILE_NAME , 'wb') as f:
		pickle.dump(names, f)
	if logs is True :
		print 'Done.'
