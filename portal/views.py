from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
	return render(request,'home.html',{})

def site_redirect(request):
	return redirect('/accounts/login')