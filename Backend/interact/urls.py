from django.conf.urls import url,include
from . import views

urlpatterns= [
	url(r'^check/$',views.MyResponseView.as_view()),
	url(r'^news_item/$',views.MyResponseView.as_view()),
	url(r'^DB/$',views.DB.as_view()),

]