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

class AI(models.Model):
	confidence=models.FloatField()

class DB(models.Model):
	yes=models.IntegerField()
	no=models.IntegerField()

# Create your models here.
