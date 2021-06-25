from LoanApp.models import Loaner, SignUp, AmountLoan, Branches, Repayment
from django.shortcuts import render, redirect




def Main(request):
	return render(request, 'mainpage.html')

def MainPage(request):
	return render(request,'mainpage.html')

def Register(request):
	return render(request,'signup.html')

def Inquire(request):
	lender = Loaner.objects.create(
		FullName = request.POST['FullName'],
		EmailAddress = request.POST['EmailAddress'],
		ResidenceAddress = request.POST['ResidenceAddress'],
		ZipCode = request.POST['ZipCode'],
		DateOfBirth = request.POST['DateOfBirth'],
		Status = request.POST['Status'],
		Citizenship = request.POST['Citizenship'],
		CellNo = request.POST['CellNo'],
		ValidID = request.POST['ValidID'],
		ValidIDNo =request.POST['ValidIDNo'],
		Income = request.POST['Income'],
		Employment = request.POST['Employment'],
		)

	return redirect('amount')
	return render(request, 'applyform.html')

def ApplyForm(request):
	return render(request, 'applyform.html')

def Borrow(request):
	aloan = AmountLoan.objects.create(
		AmountLoan = request.POST['loan'],
		Interest = request.POST['interest'],
		Months = request.POST['years'],
		MonthlyPayment = request.POST['payment'],
		TotalPayment = request.POST['total'],
		TotalInterest = request.POST['totalinterest'],
		)
	return redirect('repay_branch')
	return render(request, 'amount.html')

def Amount(request):
	return render(request, 'amount.html')

def Payment_Location(request):
	bank = Branches.objects.create(
		BankBranch = request.POST['Bank'],
		RemitanceCenter = request.POST['Remitance'],
		Location = request.POST['Location'],

		)

	pay = Repayment.objects.create(
		PaymentMethod = request.POST['PaymentMethod'],
		AccountNumber = request.POST['AccountNumber'],

		)

	return redirect('receipt')
	return render(request, 'repay_branch.html')

def Repay_Branch(request):
	return render(request, 'repay_branch.html')

def Receipt(request):
	lender = Loaner.objects.last
	aloan = AmountLoan.objects.last
	bank = Branches.objects.last
	pay = Repayment.objects.last

	context = {'lender':lender, 'aloan':aloan, 'bank':bank, 'pay':pay}
	return render(request, 'receipt.html', context)

def Details(request):
	return render(request, 'details.html')

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