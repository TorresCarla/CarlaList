from django.db import models
from django.contrib.auth.models import User

class Loaner(models.Model):
	FullName = models.TextField(default="")
	EmailAddress = models.TextField(default="")
	ResidenceAddress = models.TextField(default="")
	ZipCode = models.TextField(default="")
	DateOfBirth = models.TextField(default="")
	Status = models.TextField(default="")
	Citizenship = models.TextField(default="")
	CellNo = models.CharField(default="", max_length=12)
	Friend = models.TextField(default="")
	FriendCellNo = models.CharField(default="", max_length=12)
	ValidID = models.TextField(default="")
	ValidIDNo = models.CharField(default="", max_length=15)
	Income = models.TextField(default="")
	Employment = models.TextField(default="")

	def __str__(self):
		return self.FullName

class SignUp(models.Model):
	LoanId = models.ForeignKey(Loaner, on_delete=models.CASCADE, null=True)
	UserName = models.TextField(default="")
	Password = models.TextField(default="", max_length=10)

	def __str__(self):
		return self.UserName

class AmountLoan(models.Model):
	LoanId = models.ForeignKey(Loaner, on_delete=models.SET_NULL, null=True)
	AmountLoan = models.CharField(default="", max_length=1000000)
	Interest = models.CharField(default="", max_length=100)
	Months = models.CharField(default="",max_length=72)
	integer = models.IntegerField(default="", null=True)

	def __str__(self):
		return self.AmountLoan

class Branches(models.Model):
	LoanId = models.ForeignKey(Loaner, on_delete=models.CASCADE)
	CompanyBranch = models.TextField(default="")
	BankBranch = models.TextField(default="")
	RemitanceCenter = models.TextField(default="")
	Location = models.TextField(default="")

	def __str__(self):
		return self.Branches

class Repayment(models.Model):
	LoanId = models.ForeignKey(Loaner, on_delete=models.CASCADE)
	PaymentMethod = models.TextField(default="")
	AccountNumber = models.TextField(default="")

	def __str__(self):
		return self.Repayment

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