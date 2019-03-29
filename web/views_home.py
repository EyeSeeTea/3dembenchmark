#!/usr/bin/python
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/index.html')

def particlepicking(request):
    return render_to_response('particlepicking/index.html')

def particlepickingresults(request):
    return render_to_response('particlepicking/results/index.html')

def ctfdetection(request):
    return render_to_response('ctfdetection/index.html')

def ctfdetectionresults(request):
    return render_to_response('ctfdetection/results/index.html')

def resolutionenhancement(request):
    return render_to_response('resolutionenhancement/index.html')
