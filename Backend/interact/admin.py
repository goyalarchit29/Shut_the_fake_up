# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import news_item,AI,DB

admin.site.register(news_item)
admin.site.register(AI)
admin.site.register(DB)

# Register your models here.
