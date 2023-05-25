from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Intern, Role, RoleStatus
from .forms import InternForm, RoleForm, RoleStatusForm

# Create your views here.
# Verify if the form is valid and if the data is not duplicated
def verifyInsert(form, type, edit = False, pk = None):
    if (type == 0): # Intern
        if (edit == False):
            if (Intern.objects.filter(email=form.cleaned_data['email']).exists()):
                form.add_error('email', 'Email already associated with another intern')
                return False
            if (Intern.objects.filter(number=form.cleaned_data['number']).exists()):
                form.add_error('number', 'Number already associated with another intern')
                return False
        else:
            if (Intern.objects.filter(email=form.cleaned_data['email']).exclude(pk = pk).exists()):
                form.add_error('email', 'Email already associated with another intern')
                return False
            if (Intern.objects.filter(number=form.cleaned_data['number']).exclude(pk = pk).exists()):
                form.add_error('number', 'Number already associated with another intern')
                return False
    elif (type == 1): # Role
        if (edit == False):
            if (Role.objects.filter(name = form.cleaned_data['name']).exists()):
                form.add_error('name', 'Role already exists')
                return False
        else:
            if (Role.objects.filter(name = form.cleaned_data['name']).exclude(pk = pk).exists()):
                form.add_error('name', 'Role already exists')
                return False
    else: # RoleStatus (can only edit status, so no need to check for duplicates when editing)
        if (RoleStatus.objects.filter(role=form.cleaned_data['role'], intern=form.cleaned_data['intern']).exclude(pk = pk).exists()):
            form.add_error('role', 'Role already associated with this intern')
            return False
    return True





def interns_list(request):
    interns = Intern.objects.all()
    roles = Role.objects.all()
    internSearch = None
    roleSearch = None
    if request.GET.get('internSearch') != None:
        internSearch = request.GET.get('internSearch')
        interns = interns.filter(name__icontains=internSearch)
    if request.GET.get('roleSearch') != None:
        roleSearch = request.GET.get('roleSearch')
        roles = roles.filter(name__icontains=roleSearch)
    return render(request, 'interships/homepage.html', {'interns': interns, 'roles': roles, 'internSearch': internSearch, 'roleSearch': roleSearch})

def intern_detail(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    context = {
        'intern': intern,
        'rolestatus': RoleStatus.objects.filter(intern=intern),
    }
    return render(request, 'interships/intern_detail.html', context)


def intern_addstatus(request, pk):
    if request.method == 'GET':
        form = RoleStatusForm()
        form.fields['intern'].queryset = Intern.objects.filter(pk=pk)
        form.fields['intern'].initial = pk
        form.fields['role'].queryset = Role.objects.exclude(rolestatus__intern=pk)
        return render(request, 'interships/insert.html', {'form': form, 'type': 'Insert', 'model': 'Role Status'})
    elif request.method == 'POST':
        # Tried to do this, but changing
        # request.POST._mutable = True
        # request.POST['intern'] = pk
        form = RoleStatusForm(request.POST)
        if form.is_valid() and verifyInsert(form, 2):
            form.save()
            return redirect('intern_detail', pk=pk)
        else:
            return render(request, 'interships/insert.html', {'form': form, 'type': 'Insert', 'model': 'Role Status'})

def intern_editstatus(request, pk, rolestatus_pk):
    status = get_object_or_404(RoleStatus, pk=rolestatus_pk)
    if request.method == 'GET':
        form = RoleStatusForm(instance=status)
        form.fields['intern'].queryset = Intern.objects.filter(pk=pk)
        form.fields['role'].queryset = Role.objects.filter(pk = status.role.pk)
        return render(request, 'interships/insert.html', {'form': form, 'type': 'Edit', 'model': 'Role Status'})
    if request.method == 'POST':
        form = RoleStatusForm(request.POST, instance=get_object_or_404(RoleStatus, pk=rolestatus_pk))
        if form.is_valid():
            form.save()
            return redirect('intern_detail', pk=pk)
        else:
            return render(request, 'interships/insert.html', {'form': form, 'type': 'Edit', 'model': 'Role Status'})

def intern_deletestatus(request, pk, rolestatus_pk):
    status = get_object_or_404(RoleStatus, pk=rolestatus_pk)
    if request.method == 'GET':
        return render(request, 'interships/delete.html', {'type': "status for role: \"" + status.role.name + "\" for", 'name': status.intern.name})
    if request.method == 'POST':
        status.delete()
        return redirect('intern_detail', pk=pk)

def role_detail(request, pk):
    role = get_object_or_404(Role, pk=pk)
    context = {
        'role': role,
        'rolestatus': RoleStatus.objects.filter(role=role.pk),
    }
    return render(request, 'interships/role_detail.html', context)

def avatar(request, path):
    try:
        with open(path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpg')
    except IOError:
        raise Http404

def intern_edit(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    if request.method == 'GET':
        form = InternForm(instance=intern)
        return render(request, 'interships/insert.html', {'form': form, 'type': 'Edit', 'model': 'Intern'})
    elif request.method == 'POST':
        form = InternForm(request.POST, request.FILES, instance=get_object_or_404(Intern, pk=pk))
        if form.is_valid() and verifyInsert(form, 0, True, pk):
            # delete old avatar (if not the default one)
            if (intern.avatar != 'avatars/default.jpg'):
                intern.avatar.delete()
            form.save()
            return redirect('interns_list')
        else:
            return render(request, 'interships/insert.html', {'form': form, 'type': 'Edit', 'model': 'Intern'})

def intern_delete(request, pk):
    intern = get_object_or_404(Intern, pk=pk)
    if request.method == 'GET':
        return render(request, 'interships/delete.html', {'type': "Intern", 'name': intern})
    if request.method == 'POST':
        # Delete his avatar (if not default)
        if (intern.avatar.name != 'avatars/default.jpg'):
            intern.avatar.delete()
        # Delete all his rolestatuses
        for rolestatus in RoleStatus.objects.filter(intern=pk):
            rolestatus.delete()
        intern.delete()
        return redirect('interns_list')
    
def insertIntern(request):
    if request.method == 'GET':
        form = InternForm()
        return render(request, 'interships/insert.html', {'form': form, 'type': 'Insert', 'model': 'Intern'})
    elif request.method == 'POST':
        form = InternForm(request.POST, request.FILES)
        if form.is_valid() and verifyInsert(form, 0):
            form.save()
            return redirect('interns_list')
        else:
            return render(request, 'interships/insert.html', {'form': form, 'type': 'Insert', 'model': 'Intern'})

def insertRole(request):
    if request.method == 'GET':
        form = RoleForm()
        return render(request, 'interships/insert.html', {'form': form, 'type': 'Insert', 'model': 'Role'})
    elif request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid() and verifyInsert(form, 1):
            form.save()
            return redirect('interns_list')
        else:
            return render(request, 'interships/insert.html', {'form': form, 'type': 'Insert', 'model': 'Role'})

def role_edit(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'GET':
        form = RoleForm(instance=role)
        return render(request, 'interships/insert.html', {'form': form, 'type': 'Edit', 'model': 'Role'})
    elif request.method == 'POST':
        form = RoleForm(request.POST, instance=get_object_or_404(Role, pk=pk))
        if form.is_valid() and verifyInsert(form, 1, True, pk):
            form.save()
            return redirect('role_detail', pk=pk)
        else:
            return render(request, 'interships/insert.html', {'form': form, 'type': 'Edit', 'model': 'Role'})

def role_delete(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'GET':
        return render(request, 'interships/delete.html', {'type': "Role", 'name': role})
    if request.method == 'POST':
        # Delete all role statuses
        for rolestatus in RoleStatus.objects.filter(role=pk):
            rolestatus.delete()
        role.delete()
        return redirect('interns_list')
