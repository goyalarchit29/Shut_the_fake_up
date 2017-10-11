
import requests
import json
def getSimilarity(t1,t2):

	# try:
	t1=t1.encode('utf-8')
	t2=t2.encode('utf-8')
	print 'query  t1:',t1
	print 'search t2:',t2
	# except :
	# 	return {'similarity':'-1'}

	response = requests.post("https://twinword-text-similarity-v1.p.mashape.com/similarity/",
	  headers={
	    "X-Mashape-Key": "2S7Jn2hucCmsho8gNBoaDNzlhMVDp1nDCK7jsnXh0clbsBD9Ml",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Accept": "application/json"
	  },
	  params={
	    "text1": t1,
	    "text2": t2
	  }
	)
	print response.json()
	try:
		if response.json()['result_msg'] != 'Success' :
			print 'Error at api call sending -1'
			return {'similarity':'-1'} 
	except :
		print 'Error at api call sending -1'
		return {'similarity':'-1'}
	return response.json()



if __name__ == '__main__':
	t1="Viral video of a 13-year-old 'ragpicker addicted to solution' shows a horrifying reality".decode('utf-8')
	t2="Viral video of a 13-year-old 'ragpicker addicted to solution' shows a horrifying realityThe Indian Express 21h ago".decode('utf-8')
	print getSimilarity(t1,t2)