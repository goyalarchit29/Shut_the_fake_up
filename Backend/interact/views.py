# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json 
import requests

from .models import news_item,AI,DB

class MyResponseView(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}

	def get(self,request,*args,**kwargs):
		return HttpResponse(json.dumps(self.resp))

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		return HttpResponse(json.dumps(self.resp))


class news_item(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}

	def get(self,request,*args,**kwargs):
		return HttpResponse(json.dumps(self.resp))

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		print "Got a POST Request "
		data=self.request.GET
		item=news_item(heading=data['heading'],passage=data['passage'],author=data['author'],website=data['website'],image_link=data['image_link'])
		item.save();
		Id=item.id
		db=DB(yes=0,no=0)
		db.save()
		conf=0
		# conf=get_confidence()
		con=AI(confidence=0)
		con.save()
		return HttpResponse(" Saved Data ")



class DB(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}

	def get(self,request,*args,**kwargs):
		return HttpResponse(json.dumps(self.resp))

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		Id=self.request.GET['id']
		type=self.request.GET['type']
		obj=DB.objects.get(id=Id)
		if(type=='YES'):
			obj.yes=obj.yes+1
		else:
			obj.no=obj.no+1
		obj.save()



