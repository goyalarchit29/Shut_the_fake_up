from django.conf.urls import url,include
from . import views

urlpatterns= [
	url(r'^check/$',views.MyResponseView.as_view()),
	url(r'^news_item/$',views.news_item.as_view()),
	url(r'^init/$',views.initial.as_view()),
	url(r'^submit/$',views.submit.as_view()),




]