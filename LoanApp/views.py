from django.http import HttpResponse
from LoanApp.models import Item, Loaner
from django.shortcuts import render, redirect

def MainPage(request):
	return render(request, 'mainpage.html')

def ViewList(request, LoanId):
	lId = Loaner.objects.get(id=LoanId)
	return render(request, 'LoanAF.html', {'LoanId': lId})

def NewList(request):
	newLoaner = Loaner.objects.create()
	Item.objects.create(LoanId=newLoaner, text=request.POST['FullName'])
	return redirect(f'/LoanApp/{newLoaner.id}/')

def AddItem(request,lId):
	lId = Loaner.objects.get(id=lId)
	Item.objects.create(LoanId=lId,text=request.POST['FullName'])
	return redirect(f'/LoanApp/{lId.id}/')


	#if request.method == 'POST':
		#Item.objects.create(text=request.POST['Newmember'])
		#return redirect('/LoanApp/viewlist_url/')
