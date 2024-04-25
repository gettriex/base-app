from django.shortcuts import render
from django.views.generic import ListView

from .models import *
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def company(request):
    return render(request, 'main/company.html')


def login(request):
    return render(request, 'main/login.html')

