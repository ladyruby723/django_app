from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is a blog/polls application, built with the Django web framework for Python.")

