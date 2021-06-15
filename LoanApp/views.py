from django.http import HttpResponseRedirect
from LoanApp.models import SignUp, Loaner
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.contrib.auth.models import User

def MainPage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('afterlogin')
		return render(request,'mainpage.html')

def SignUp(request):
		return render(request,'signup.html')

def LoanAF(request):
	return render(request, 'LoanAF.html')

def AboutUs(request):
	return render(request, 'aboutus.html')

def Contacts(request):
	return render(request, 'contacts.html')

def ViewList(request, LoanId):
	lId = Loaner.objects.get(id=LoanId)
	return render(request, 'LoanAF.html', {'LoanId': lId})

def NewList(request):
	newLoaner = Loaner.objects.create()
	SignUp.objects.create(LoanId=newLoaner, username=request.POST['FullName'])
	return redirect(f'/LoanApp/{newLoaner.id}/')

def AddSignUp(request,lId):
	lId = Loaner.objects.get(id=lId)
	SignUp.objects.create(LoanId=lId,username=request.POST['FullName'])
	return redirect(f'/LoanApp/{lId.id}/')
	


	#if request.method == 'POST':
	#Item.objects.create(text=request.POST['FullName'])
	#return redirect('/LoanApp/viewlist_url/')
#return render(request,'mainpage.html')
#items = Item.objects.all()

#def MainPage(request):
#	if request.method == 'POST':
#		newItem = request.POST['FullName']
#		Item.objects.create(text=newItem)
#	else:
#		newItem = ''
#	return render(request, 'mainpage.html',{'NewFullName': newItem,})

	# item1 = Item()
	# item1.text=request.POST.get('FullName', '')
	# item1.save()
	# #return render(request,'mainpage.html',{'NewFullName':request.POST.get('FullName',''),})
	# return render(request,'mainpage.html',{'NewFullName': item1.text,})



'''
# Create your views here.
#def MainPage(request):
#	return render(request,'mainpage.html',{'NewFullName':request.POST.get('FullName'),'NewEmailAddress':request.POST.get('EmailAddress',''),})

#if request.method == 'POST':
#return HttpResponse(request.POST['FullName'])
#return render(request,"mainpage.html")
#def MainPage(request):
'''
