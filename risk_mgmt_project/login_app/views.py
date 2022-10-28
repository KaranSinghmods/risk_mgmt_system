from django.shortcuts import render

# Create your views here.

# Call Hello World at root of our application
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world!")