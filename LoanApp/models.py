from django.db import models

# Create your models here.
class Recruit(models.Model):
	pass
class Item(models.Model):
	RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	text = models.TextField(default="")


	#addr = models.IntField(default="")
	#addrSt = models.CharField(default="")
