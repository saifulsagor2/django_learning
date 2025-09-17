from dhango.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("This is courses page")
