from django.shortcuts import render
from django.http import HttpResponse

# def calculate():
#     x = 1
#     y = 2
#     return x

def todo(request):
    # x = calculate()
    return render(request, 'todo.html', {'name' : 'Testing!'})
