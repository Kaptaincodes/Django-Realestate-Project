from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    """ Here we return the index page """
    return render(request, 'pages/index.html')

def about(request):
    """ """
    return render(request, 'pages/about.html')