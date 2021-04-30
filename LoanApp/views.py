from django.shortcuts import render,redirect
from django.http import HttpResponse
from LoanApp.models import Item

def MainPage(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['FullName'])
		return redirect('/LoanApp/viewlist_url/')
	#return render(request,'mainpage.html')
	items = Item.objects.all()
	return render(request, 'mainpage.html', {'NewFullName': items})

def ViewList(request):
	items = Item.objects.all()
	return render(request, 'mainpage.html', {'NewFullName': items})

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