from django.conf.urls import url
from LoanApp import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	url(r'^$', views.MainPage, name='mainpage'),
  	url(r'^LoanApp/signup', views.LoanAF, name='signup'),
    url(r'^LoanApp/LoanAF', views.LoanAF, name='loanaf'),
    url(r'^LoanApp/aboutus', views.AboutUs, name='aboutus'), 
    url(r'^LoanApp/contacts', views.Contacts, name='contacts'),
    url(r'^LoanApp/(\d+)/$', views.ViewList, name='viewlist'),
    url(r'^LoanApp/newlist_url$', views.NewList, name='newlist'),
    url(r'^LoanApp/(\d+)/AddSignUp$', views.AddSignUp, name='addsigup'),
]

"""CarlaList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""