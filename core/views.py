from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

def index_view(request):
    return render(request, 'core/index.html')