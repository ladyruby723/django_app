from django.shortcuts import render
from django.http import HttpResponse

# Create views

def index(request):
    return HttpResponse("This is a blog/polls application, built with the Django web framework for Python.")

def detail(request, question_id):
    return HttpResponse("Question %s." % question_id)

def results(request, question_id):
    response = "Results for question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s." % question_id)
