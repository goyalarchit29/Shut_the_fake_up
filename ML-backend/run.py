import pickle 
from get_sources import generate_maybe_sources_file,SOURCES_FILE_NAME


generate_maybe_sources_file()

with open(SOURCES_FILE_NAME,'rb') as f :
	s_names = pickle.load(f) 

print s_names


