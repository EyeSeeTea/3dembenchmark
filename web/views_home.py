#!/usr/bin/python
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/index.html')

def page(request):
    return render_to_response('page/index.html')

def ctf(request):
    return render_to_response('ctf/index.html')
