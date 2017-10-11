import requests
from bs4 import BeautifulSoup
from apirequest import getSimilarity
from fakesite import verifyLink
# https://market.mashape.com/settings/transactions/59dcac28e4b0ebde65517745 
# check api requests here.
link = 'https://news.google.com/news/search/section/q/'
k = {
"`" : "%60",
"[" : "%5B",
"]" : "%5D",
"\\" : "%5C",
";" : "%3B",
"," : "%2C",
" " : "%20",
"/" : "%2F"

}

def convert(s):
	for key,val in k.iteritems():
		s = s.replace(key,val)
	return  s+'/'+s+'?hl=en&ned=us'


def getConfidence(query,website=False):
	# query = 'leaked%20email/leaked%20email?hl=en&ned=us'
	# query = raw_input()
	queryconverted = convert(query)
	mlink = link + queryconverted
	print mlink
	# mlink = "https://news.google.com/news/search/section/q/leaked%20email/leaked%20email?hl=en&ned=us"
	LIMIT = 10

	r = requests.get(mlink)
	soup = BeautifulSoup(r.text,'html.parser')
	blocks = soup.find_all('c-wiz',{"class":"M1Uqc kWyHVd"})
	result = []
	resultlink = []
	i =0 
	for block in blocks :
		i+= 1 
		if i >LIMIT :
			# limiting upto 10 calls
			break
		rr = block.find('a',{"class":"nuEeue hzdq5d ME7ew"})

		result.append(rr.text)
		resultlink.append(rr.get('href'))
		print rr.text
		print '*'*50
	# print result
	confidence = 0 	
	if len(result) == 0 :
		print 'No result.'
		# --------------------------- RETURN ---------------------------
		return confidence,'No Link Found'

	if website is True :
		# return 0.1,'test'


		finaltext = '. '.join(result)
		ll = len(result)
		finalquery = (query+' ')*ll
		print 'FINAL TEXT  :',finaltext
		print 'FINAL QUERY :',finalquery
		ans = getSimilarity(finalquery,finaltext)
		print ans
		total = 0
		# i = 0
		# while(i<3 and i<ll):
		# 	x = verifyLink(resultlink[i])
		# 	if x == 0 :
		# 		total -= 3 #more penalty.
		# 	else :
		# 		total += 1 #less praise.
		# 	i+=1
		# total = float(total) / ((i-1)*4)
		# print 'Total',total
		for rlink in resultlink :
			if 'faking' in rlink :
				confidence = 0



		confidence =  ans['similarity']
		maxconfidencelink = 'NoneSent'
		print 'confidence        :',confidence 
		print 'maxconfidencelink :', maxconfidencelink
		if confidence <0 :
			confidence = 0

	# --------------------------- RETURN ---------------------------
		return confidence,maxconfidencelink

	else:

		sim = []
		i=0
		for item in result :
			i+=1
			ans = getSimilarity(query,item)
			print 'Item:'+str(i)+'/'+str(len(result))+' '+str(ans)
			sim.append(float(ans['similarity']))
		# mu = listmean(sim)
		print 'SIMILARITIES:',sim

		# confidence = max(sim)
		# idx = sim.index(max(sim))
		# print sim 
		# print resultlink
		sim, resultlink = zip(*sorted(zip(sim, resultlink) , reverse=True))
		i=0
		sim=[z for z in sim]
		resultlink = [zz for zz in resultlink]
		l = len(sim)
		print 'l',l
		while(i<3 and i<l):
			x = verifyLink(resultlink[i])
			sim[i] = sim[i]*x
			i+=1

		sim, resultlink = zip(*sorted(zip(sim, resultlink) , reverse=True))

		confidence = sim[0]
		maxconfidencelink = resultlink[0]
		print 'confidence:',confidence
		print 'maxconfidencelink', maxconfidencelink

	# --------------------------- RETURN ---------------------------
	return confidence,maxconfidencelink



if __name__ == "__main__":
	query = raw_input('>Input Query News:')
	x = getConfidence(query,True)
	












