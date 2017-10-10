from django.conf.urls import url,include
from . import views

urlpatterns= [
	url(r'^check/$',views.MyResponseView.as_view()),
]