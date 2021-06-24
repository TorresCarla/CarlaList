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
	LoanId = SignUp.objects.create(
	username = request.POST['username'],
	password = request.POST['password'],
	)
	return redirect(request,'ApplyForm')
	return render(request,'signup.html')

def ApplyForm(request):
	LoanId = Loaner.objects.create(
	FullName = request.POST['FullName'],
	EmailAddress = request.POST['EmailAddress'],
	CellNo = request.POST['CellNo'],
	Friend = request.POST['Friend'],
	FriendCellNo = request.POST['FriendCellNo'],
	ValidID = request.POST['ValidID'],
	ValidIDNo =request.POST['ValidIDNo'],
	Income = request.POST['Income'],
	Employment = request.POST['Employment'],
	)
	return redirect(request,'Receipt')
	return render(request,'applyform.html')

def Amount(request):
	LoanId = AmountLoan.objects.create(
	AmountLoan = request.POST['loan'],
	Interest = request.POST['interest'],
	Months = request.POST['months'],
)
	return redirect(request,'Receipt')
	return render(request, 'amount.html')

def Repay_Branch(request):
	LoanId = Branches.objects.create(
	BankBranch = request.POST['Bank'],
	RemitanceCenter = request.POST['Remitance'],
	Location = request.POST['Location'],
	)
	LoanId = Repayment.objects.create(
	PaymentMethod = request.POST['PaymentMethod'],
	AccountNumber = request.POST['AccountNumber'],
	)
	return redirect(request,'Receipt')
	return render(request, 'repay_branch.html')

def Receipt(request):
	FullName = Loaner.objects.filter()
	EmailAddress = Loaner.objects.filter()
	CellNo = Loaner.objects.filter()
	AmountLoan = AmountLoan.objects.filter()
	Interest = AmountLoan.objects.filter()
	Months = AmountLoan.objects.filter()
	BankBranch = Branches.objects.filter()
	RemitanceCenter = Branches.objects.filter()
	Location = Branches.objects.filter()
	PaymentMethod = Repayment.objects.filter()
	AccountNumber = Repayment.objects.filter()
	context = {'FullName':FullName , 
		'EmailAddress':EmailAddress , 
		'CellNo':CellNo , 
		'loan':loan , 
		'interest':interest , 
		'months':months , 
		'payment':payment ,
		'Bank':Bank , 
		'Remitance':Remitance,
		'Location':Location ,
		'PaymentMethod':PaymentMethod ,
		'AccountNumber':AccountNumber  }
	return render(request, 'receipt.html', context)

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
