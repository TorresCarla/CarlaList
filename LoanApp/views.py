from django.http import HttpResponseRedirect
from LoanApp.models import Loaner, SignUp, AmountLoan, Branches, Repayment
from django.shortcuts import render,redirect



def Main(request):
	return render(request, 'mainpage.html')

def ViewList(request, LoanId):
	lId = Loaner.objects.get(id=LoanId)
	return render(request, 'mainpage.html', {'LoanId': lId})

def NewList(request):
	newLoaner = Loaner.objects.create()
	SignUp.objects.create(username=request.POST['FullName'])
	return redirect(f'/LoanApp/{newLoaner.id}/')

def MainPage(request):
	return render(request,'mainpage.html')

def SignUp(request):
	return render(request,'signup.html')

def LogIn(request):
	return render(request,'login.html')

def ForgotPassword(request):
	return render(request,'forgotpassword.html')

def Reset(request):
	return render(request,'reset.html')

def ApplyForm(request):
	return render(request,'applyform.html')

def Amount(request):
	return render(request, 'amount.html')

def Repay_Branch(request):
	return render(request, 'repay_branch.html')

def Payment(request):
	return render(request, 'payment.html')

def AboutUs(request):
	return render(request, 'aboutus.html')

def Contacts(request):
	return render(request, 'contacts.html')




	


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
