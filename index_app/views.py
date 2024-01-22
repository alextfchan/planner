from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Index Page")

# def index(request):
#     return render(request, 'home.html')

def index(request):
    return render(request,'home.html')