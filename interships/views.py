from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Intern, Role, RoleStatus

# Create your views here.
def interns_list(request):
    context = {
        'interns': Intern.objects.all(), 
        'roles': Role.objects.all(),
    }
    return render(request, 'interships/homepage.html', context)

def intern_detail(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    context = {
        'intern': intern,
        'rolestatus': RoleStatus.objects.filter(intern=intern),
    }
    return render(request, 'interships/intern_detail.html', context)

def avatar(request, path):
    try:
        with open('./avatars/' + path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpg')
    except IOError:
        raise Http404

def intern_edit(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    context = {
        'intern': intern,
        'roles': Role.objects.all(),
    }
    return render(request, 'interships/intern_edit.html', context)
def insert(request):
    return HttpResponse("<h1>On The Works!!</h1>")