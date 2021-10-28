from django.http.response import HttpResponse
from django.shortcuts import render
from .services import *

# Create your views here.

def index(request):
    
    return render(request, 'app/index.html')