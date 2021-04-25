from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def MainPage(request):
	return render(request,'mainpage.html',{'NewFullName': request.POST.get('FullName'),'NewEmailAddress': request.POST.get('EmailAddress',''),})

#if request.method == 'POST':
#return HttpResponse(request.POST['FullName'])
#return render(request,"mainpage.html")
#def MainPage(request):