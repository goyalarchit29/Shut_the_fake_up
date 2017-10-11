# import requests

# from apirequest import getSimilarity
# # https://market.mashape.com/settings/transactions/59dcac28e4b0ebde65517745 
# # check api requests here.
# k = {
# "`" : "%60",
# "[" : "%5B",
# "]" : "%5D",
# "\\" : "%5C",
# ";" : "%3B",
# "," : "%2C",
# " " : "%20",
# "/" : "%2F"

# }

# def convert(s):
# 	for key,val in k.iteritems():
# 		s = s.replace(key,val)
# 	return  s+'/'+s+'?hl=en&ned=us'


# link = 'https://news.google.com/news/search/section/q/'
# # query = 'leaked%20email/leaked%20email?hl=en&ned=us'
# query = raw_input()
# queryconverted = convert(query)
# mlink = link + queryconverted
# print mlink
# # mlink = "https://news.google.com/news/search/section/q/leaked%20email/leaked%20email?hl=en&ned=us"
# from bs4 import BeautifulSoup

# # def listmean(a):
# # 	total = 0 :
# # 	for x in a :
# # 		total += x
# # 	mean = float(total)/len(a)
# # 	return mean

# r = requests.get(mlink)
# soup = BeautifulSoup(r.text,'html.parser')
# blocks = soup.find_all('c-wiz',{"class":"M1Uqc kWyHVd"})

# result = []
# for block in blocks :
# 	rr = block.find('a',{"class":"nuEeue hzdq5d ME7ew"})
# 	result.append(rr.text)
# 	print rr.text
# 	print '*'*50