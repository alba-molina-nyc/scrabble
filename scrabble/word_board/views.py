from typing import List
from django.shortcuts import render
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'index.html')

# def index(request):
#     return HttpResponse("hi")



