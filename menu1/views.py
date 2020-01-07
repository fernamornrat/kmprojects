from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    return render(request ,'menu1/index.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')