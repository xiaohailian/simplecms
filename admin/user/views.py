from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse

def user(request):
    return HttpResponse('user')