from curses.ascii import HT
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
	return HttpResponse('<h1>THis is the HOOMe</h1>')

def mul(request, a, b, c):
	return HttpResponse(int(a)*int(b)*int(c))

def hps(request):
	return render(request, "Pages/index.html")

def movie(request):
	return render(request, "Pages/movie.html")

def register(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		plan_type = request.POST.get("plan_type")
		password = request.POST.get("password")
		if request.FILES:
			file = request.FILES["pic"]
			fs = FileSystemStorage()
			savedfile = fs.save(file.name, file)
			file_url = fs.url(savedfile)
		
		return HttpResponse("Form submitted successfully. Data got is {} {} {} {}  <img src = '{}'> ". format(name, email, plan_type, password, file_url))
	return render(request, "Pages/register.html")
