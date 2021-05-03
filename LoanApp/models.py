from django.db import models

class Loaner(models.Model):
	pass

class Item(models.Model):
	LoanId = models.ForeignKey(Loaner, default=None, on_delete=models.CASCADE)
	text = models.TextField(default="")
	#addr = models.IntField(default="")
	#addrSt = models.CharField(default="")


# Create your models here.