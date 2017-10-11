path = 'api_keys'
import pickle

API_KEYS_FILE = 'api.keys'

def if_api_keys_exists():
	# check for API_KEYS_FILE
	cur_dir = os.getcwd()
	file_list = os.listdir(cur_dir)
	if API_KEYS_FILE in file_list :
		return True
	return False


def saveModify_keys():
	d = {}
	if if_api_keys_exists():
		with open(API_KEYS_FILE,'rb') as f:
			d = pickle.load(f)
	ask = True
	while ask :
		print 'Name of Api: '
		name = raw_input()
		print 'Api Key: '
		key = raw_input()
		d['name'] = key
		print 'More? y/n'
		ask = raw_input()

		if ask=='y' or ask=='Y':
			ask = True
		else :
			ask = False

	with open(API_KEYS_FILE,'wb') as f:
		pickle.dump(d,f)

def read_key(name):
	with open(API_KEYS_FILE,'rb') as f:
		d = pickle.load(f)
	try:
		return d[name]
	except :
		return ''

if __name__ == '__main__' :
	saveModify_keys()