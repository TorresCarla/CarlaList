from django.http import HttpResponse
from LoanApp.models import SignUp, Loaner
from django.shortcuts import render, redirect

def MainPage(request):
	return render(request, 'mainpage.html')

def ViewList(request, LoanId):
	lId = Loaner.objects.get(id=LoanId)
	return render(request, 'LoanAF.html', {'LoanId': lId})

def NewList(request):
	newLoaner = Loaner.objects.create()
	Item.objects.create(LoanId=newLoaner, signup=request.POST['FullName'])
	return redirect(f'/LoanApp/{newLoaner.id}/')

def AddItem(request,lId):
	lId = Loaner.objects.get(id=lId)
	Item.objects.create(LoanId=lId,signup=request.POST['FullName'])
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
