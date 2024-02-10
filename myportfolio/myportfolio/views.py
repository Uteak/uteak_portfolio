from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    # pass
    # return HttpResponse("main index")
    return render(request, 'index.html')
