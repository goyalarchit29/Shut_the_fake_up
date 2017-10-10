# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json 
import requests

class MyResponseView(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}

	def get(self,request,*args,**kwargs):
		print "Got a GET Request"
		data=self.request.GET
		print data
		return HttpResponse(json.dumps(self.resp))

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		print "Got a POST Request "
		data=json.loads(self.request.GET)
		print data
		return HttpResponse(json.dumps(self.resp))


class DB(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}

	def get(self,request,*args,**kwargs):
		data=self.request.GET
		id=data['id']
		vote=data['vote']
		return HttpResponse(json.dumps(self.resp))

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		return HttpResponse(" Empty Response ")


class MyResponseView(generic.View):

	def __init__(self):
		self.resp={'Status':'Success ! Star Wars '}

	def get(self,request,*args,**kwargs):
		print "Got a GET Request"
		data=self.request.GET
		print data
		return HttpResponse(json.dumps(self.resp))

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		print "Got a POST Request "
		data=json.loads(self.request.GET)
		print data
		return HttpResponse(json.dumps(self.resp))




# Create your views here.
