from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def MainPage(request):
	return HttpResponse('<html><title>Recipe List</title><h1 style="color:blue; font-size=35px">Three Main Course Recipe List</h1><input type="text" id="newEntry" name="Entry1" placeholder="What recipe do you want to request&#063">&nbsp<input type="submit" value="Confirm"></html')

