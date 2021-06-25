from django.db import models
from django.utils import timezone

class Loaner(models.Model):
	FullName = models.TextField(default="", null=True)
	EmailAddress = models.TextField(default="")
	ResidenceAddress = models.TextField(default="")
	ZipCode = models.TextField(default="")
	DateOfBirth = models.TextField(default="")
	Status = models.TextField(default="")
	Citizenship = models.TextField(default="")
	CellNo = models.TextField(default="", max_length=12)
	ValidID = models.TextField(default="")
	ValidIDNo = models.CharField(default="", max_length=15)
	Income = models.TextField(default="")
	Employment = models.TextField(default="")

	def __str__(self):
		return self.FullName

class SignUp(models.Model):
	LoanId = models.ForeignKey(Loaner, null=True, on_delete=models.CASCADE)
	UserName = models.TextField(default="")
	Password = models.TextField(default="", max_length=10)

	def __str__(self):
		return self.UserName

class AmountLoan(models.Model):
	LoanId = models.ForeignKey(Loaner, null=True, on_delete=models.CASCADE)
	AmountLoan = models.CharField(default="", max_length=1000000)
	Interest = models.CharField(default="", max_length=100)
	Months = models.CharField(default="",max_length=72)
	MonthlyPayment = models.CharField(default="", max_length=100000)
	TotalPayment = models.CharField(default="", max_length=1000000)
	TotalInterest = models.CharField(default="", max_length=1000000)
	def __str__(self):
		return self.AmountLoan

class Branches(models.Model):
	LoanId = models.ForeignKey(Loaner, null=True, on_delete=models.CASCADE)
	BankBranch = models.TextField(default="")
	RemitanceCenter = models.TextField(default="")
	Location = models.TextField(default="")

	def __str__(self):
		return self.BankBranch

class Repayment(models.Model):
	LoanId = models.ForeignKey(Loaner, null=True, on_delete=models.CASCADE)
	PaymentMethod = models.TextField(default="")
	AccountNumber = models.TextField(default="")

	def __str__(self):
		return self.PaymentMethod

#class Interest(models.Model):
#	Interest = models.CharField(default="InProcess", max_length=100)
#	integer = models.IntegerField(null=True)
#
#	def __str__(self):
#		return self.Interest
#
#class Months(models.Model):
#	Months = models.CharField(default="InProcess",max_length=72)
#	integer = models.IntegerField(null=True)
#
#	def __str__(self):
#		return self.Months

	#addr = models.IntField(default="")
	#addrSt = models.CharField(default="")

#class Item(models.Model):
#	LoanId = models.ForeignKey(Loaner, default="", on_delete=models.CASCADE)
#	Friend = models.TextField(default="")
#	FriendCellNo = models.CharField(default="", max_length=12)
#
#	def __str__(self):
#		return self.Friend

#class ValidID(models.Model):
#	LoanId = models.ForeignKey(Loaner, default="", on_delete=models.CASCADE)
#	ValidID = models.TextField(default="")
#	ValidIDNo = models.CharField(default="", max_length=15)
#
#	def __str__(self):
#		return self.ValidID

#class Employment(models.Model):
#	LoanId = models.ForeignKey(Loaner, default="", on_delete=models.CASCADE)
#	Income = models.TextField(default="")
#	Employment = models.TextField(default="")
#
#	def __str__(self):
#		return self.Employment
# Create your models here.