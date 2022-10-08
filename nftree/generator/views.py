from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(_request):
    return HttpResponse("<h1>Hello World.</h1> You're at the Generator App.")