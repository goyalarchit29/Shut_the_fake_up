# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class  news(models.Model):
    id = votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


# Create your models here.
