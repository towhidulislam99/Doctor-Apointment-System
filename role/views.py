from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Role


def index(requset):
    return render(requset, 'admin/role.html')

def insert(requset):
    role = requset.POST.get('role')
    if(len(role)==0):
        return HttpResponse('Empty Fields not be acceptted')
    else:
        role_obj = Role()
        role_obj.name = role
        role_obj.save()
        return redirect('roleoutput')
    
    
def roleoutput(request):
    all_data = Role.objects.all()
    if(len(all_data)==0):
        status = False
    else:
        status = True
    data = {"role_data": all_data, 'status': status}
    return render(request,'admin/role.html', data)

def role_edit(request, id):
    all_data = Role.objects.get(id=id)
    data = {"role_data": all_data}
    return render(request,'admin/roleUpdate.html', data)

def update(request):
    id = request.POST.get('id')
    name = request.POST.get('role')
    
    role_obj = get_object_or_404(Role, id=id)
    role_obj.name = name
    role_obj.save()
    return redirect('roleoutput')

def delete_role(request, id):
    role_obj = get_object_or_404(Role, id=id)
    role_obj.delete()
    return redirect('roleoutput')