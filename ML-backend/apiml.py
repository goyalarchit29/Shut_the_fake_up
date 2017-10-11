#!flask/bin/python
from flask import Flask ,request, jsonify, Response , render_template
from flask_cors import CORS, cross_origin
from confidence import getConfidence
import json
app = Flask(__name__)
CORS(app)
WTF_CSRF_ENABLED = True
from flask_httpauth import HTTPBasicAuth

@app.route('/')
def hi():
	return 'Hello World'




@app.route('/getconf', methods=['POST','GET'])
def conf():
	print 'REQUEST METHOD:',request.method
	# print 'REQUEST ARGS  :',request.args
	print 'REQUEST:',request
	print 'REQUEST ARGS',request.args
	print 'REQUEST DATA',request.data
	print 'REQUEST json:',request.json

	print '*'*50
	query = ''
	website = False

	if str(request.method) == 'GET':
		query=str(request.args.get('headline'))
		website = True
		# query = str(request.args.to_dict().get('headline'))
		# print query
	else :
		query = request.json["headline"]

	print 'Query:'+str(query)
	c,l = getConfidence(query,website)
	resp = {'confidence': c,'maxconflink':l}
	resp = Response(response=json.dumps(resp),status=200)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	print resp
	return render_template('hello.html', query= query, conf=c)
	# return resp


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')