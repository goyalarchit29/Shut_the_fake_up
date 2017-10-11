check = "%601234567890qwertyuiop%5B%5D%5Casdfghjkl%3B'zxcvbnm%2C.%2F/%601234567890qwertyuiop%5B%5D%5Casdfghjkl%3B'zxcvbnm%2C.%2F?hl=en&ned=us"

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



if __name__ == '__main__':
	check = "o%3BiIOEUOQ%20ASJDK%20DFR394U8NAMF%20DFAW'D%3B%20adjfl%3Bakdsjf/o%3BiIOEUOQ%20ASJDK%20DFR394U8NAMF%20DFAW'D%3B%20adjfl%3Bakdsjf?hl=en&ned=us"
	q = "o;iIOEUOQ ASJDK DFR394U8NAMF DFAW'D; adjfl;akdsjf"
	final = convert(q)
	# print '*'*20
	if final == check :
		print 'True'
