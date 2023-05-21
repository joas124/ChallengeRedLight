from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Intern, Role, RoleStatus

# Create your views here.
def interns_list(request):
    interns = Intern.objects.all()
    roles = Role.objects.all()
    return render(request, 'interships/homepage.html', {'interns': interns, 'roles': roles})

def intern_detail(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    return render(request, 'interships/intern_detail.html', {'intern': intern, 'rolestatus': RoleStatus.objects.filter(intern=intern)})

def avatar(request, path):
    try:
        with open('./avatars/' + path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpg')
    except IOError:
        raise Http404

def intern_edit(request, pk):
    return HttpResponse("<h1>On The Works!!</h1>")
def insert(request):
    return HttpResponse("<h1>On The Works!!</h1>")