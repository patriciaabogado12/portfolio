from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'github/index.html')

def patricia(request):
    return render(request, 'github/patricia.html')

def mechaila(request):
    return render(request, 'github/mechaila.html')

