from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def interns_list(request):
    return HttpResponse('<h1>Interns List:</h1>')

def intern_detail(request, pk):
    return HttpResponse('<h2>Details for intern:' + str(pk) + '</h2>')