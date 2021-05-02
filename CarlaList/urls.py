from django.conf.urls import url
from LoanApp import views

urlpatterns = [
	url(r'^$', views.MainPage, name='mainpage'),
	url(r'^LoanApp/(\d+)/$', views.ViewList, name='viewlist'),
	url(r'^LoanApp/newlist_url$', views.NewList, name='newlist'),
	url(r'^LoanApp/(\d+)/addItem$', views.AddItem, name='additem'),	
]

