from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='mainpage'),
    path('mainpage', views.MainPage, name='mainpage'),
    path('signup', views.Register, name='signup'),
    path('inquire', views.Inquire, name='inquire'),
    path('applyform', views.ApplyForm, name='applyform'),
    path('borrow', views.Borrow, name='borrow'),
    path('amount', views.Amount, name='amount'),
    path('payment_location', views.Payment_Location, name='payment_location'),
    path('repay_branch', views.Repay_Branch, name='repay_branch'),
    path('receipt', views.Receipt, name='receipt'), 
    path('details', views.Details, name='details'), 
    path('aboutus', views.AboutUs, name='aboutus'), 
    path('contacts', views.Contacts, name='contacts'),

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