from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Intern, Role, RoleStatus
from .forms import InternForm, RoleForm

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

def role_detail(request, pk):
    role = get_object_or_404(Role, pk=pk)
    context = {
        'role': role,
        'rolestatus': RoleStatus.objects.filter(role=role),
    }
    return render(request, 'interships/role_detail.html', context)

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

def insertIntern(request):
    if request.method == 'GET':
        form = InternForm()
        return render(request, 'interships/insert.html', {'form': form})
    elif request.method == 'POST':
        form = InternForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('interns_list')
        else:
            return render(request, 'interships/insert.html', {'form': form})

def insertRole(request):
    if request.method == 'GET':
        form = RoleForm()
        return render(request, 'interships/insert.html', {'form': form})
    elif request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interns_list')
        else:
            return render(request, 'interships/insert.html', {'form': form})
