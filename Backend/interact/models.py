# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


 
class news_item(models.Model):
	date=models.DateField(auto_now_add=True)
	heading=models.TextField()
	passage=models.TextField()
	author=models.CharField(max_length=200,default="rowling")
	website=models.CharField(max_length=200,default="rowling")
	image_link=models.CharField(max_length=200,default="rowling")
	confidence=models.FloatField(default=0)
	yes=models.IntegerField(default=0)
	no=models.IntegerField(default=0)

class state(models.Model):
	story_no=models.IntegerField(default=0)

# Create your models here.
