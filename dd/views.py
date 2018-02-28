from django.http import HttpResponse
import sys

def hello(request):
    data = str(sys.path)
    return HttpResponse(data)

def main(request):
    return HttpResponse('Main Page.')