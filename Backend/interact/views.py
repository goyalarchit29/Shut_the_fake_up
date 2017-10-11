# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json 
import requests
import tweepy


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)


def tweet(headline):
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "W701fEkTxIMaqa9ka6QV5T05O",
    "consumer_secret"     : "hQOZp3hr3BacHK0SZNkP96Up7axQEGGwvid5GmHEt9CJLALlci",
    "access_token"        : "917868221709008896-ilWT2rXzl5GQOy13RwNQ93QtKvNV1lR",
    "access_token_secret" : "WHRJlVa7yV7QJhTNBJLzn13addmLil1srOWwYoYwnY8Nx" 
    }

  api = get_api(cfg)
  tweet = "Fake News Alert ! \n "+headline
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing


############

from .models import news_item as news_item_model,state as tweet_state

class MyResponseView(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}

	def get(self,request,*args,**kwargs):
		R=HttpResponse(json.dumps(self.resp))
		R["Access-Control-Allow-Headers"] = "*"
		return R

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		R=HttpResponse(json.dumps(self.resp))
		R["Access-Control-Allow-Headers"] = "*"
		return R



class news_item(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}
	def get(self,request,*args,**kwargs):   
		# Send list of news articles

		news_articles=[{'id':it.id,'heading':it.heading,'date':str(it.date),'passage':it.passage,'author':it.author,'website':it.website,'image_link':it.image_link,'confidence':it.confidence,'yes':it.yes,'no':it.no} for it in  news_item_model.objects.all()]
		# print news_articles
		news_articles=sorted(news_articles,key=lambda x:x['id'],reverse=True)
		print news_articles
		response={'news_items':news_articles}
		R=HttpResponse(json.dumps(response))
		R["Access-Control-Allow-Headers"] = "*"
		return R

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		print "Got a POST Request "
		data=self.request.POST
		print "This is the post request "
		print data['image_link']
		item=news_item_model(heading=data['heading'],passage=data['passage'],author=data['author'],website=data['website'],image_link=data['image_link'])
		item.save();
		Id=item.id
		db=DB_model(yes=0,no=0)
		db.save()
		print " Saved "
		conf=0
		# conf=get_confidence()
		con=AI_model(confidence=0)
		con.save()
		R=HttpResponse(" Saved Data ")
		R["Access-Control-Allow-Headers"] = "*"
		return R



class submit(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}
	def get(self,request,*args,**kwargs):   
		R=HttpResponse(" Go home baby !")
		R["Access-Control-Allow-Headers"] = "*"
		return R


	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		print("Posting")
		# print self.request.POST['PostData']
		data=self.request.POST['PostData']
		print data
		data=str(data)
		data=json.loads(data)
		print type(data)
		# print data
		Id=data['id']
		ob=news_item_model.objects.filter(id=Id)[0]
	
		if(data['type']=='1'):
			# news_item_model.objects.filter(id=Id).update(yes=y+1)
			ob.yes=ob.yes+1
		else:
			# news_item_model.objects.filter(id=Id).update(no=n+1)
			ob.no=ob.no+1
		ob.save()
		y=((float(ob.yes)/(ob.yes+ob.no))*3+ob.confidence)/4
		n=((float(ob.no)/(ob.yes+ob.no))*3+1-ob.confidence)/4
		R=HttpResponse(json.dumps({'id':Id,'yes':str(int(y*100)),'no':str(int(n*100)),'confidence':ob.confidence}))
		R["Access-Control-Allow-Headers"] = "*"
		print ob.heading+" -- " +str(n) 
		if(n>=0.5):
			tweeted_ones=tweet_state.objects.filter(story_no=Id)
			if(len(tweeted_ones)==0):
				tweeted=tweet_state(story_no=Id)
				tweeted.save()
				tweet(ob.heading)
		return R




# -*- coding: utf-8 -*-

class initial(generic.View):


	def get(self,request,*args,**kwargs):
		url='http://192.168.43.210:5000/getconf'

		news_items=news_item_model.objects.all()
		naya_items=[]

		for x in news_items:
			Str=str(x.heading)
			params={'headline':Str}
			re=requests.post(url,json=params)
			print re.text
			data=json.loads(re.text)
			y=x
			y.confidence=data['confidence']
			naya_items.append(y)

		for y in naya_items:
			y.save()

		R=HttpResponse("Done Dana")
		R["Access-Control-Allow-Headers"] = "*"
		return R

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		R=HttpResponse("")
		R["Access-Control-Allow-Headers"] = "*"
		return R






