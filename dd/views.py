from django.http import HttpResponse
import sys
import datetime

def hello(request):
    data = str(sys.path)
    return HttpResponse(data)

def main(request):
    return HttpResponse('Main Page.')

def ls(request):
    return HttpResponse('ls')

def time(req):
    return HttpResponse(datetime.datetime.now())