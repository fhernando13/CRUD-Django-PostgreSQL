from gc import get_objects
from django.shortcuts import render, redirect,  get_object_or_404
from testuser.models import User
from testuser.form import Userform

# Create your views here.
def detalle(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'detalle.html', {'user':user})

def Agregar(request):
    if request.method == 'POST':
        formaUser = Userform(request.POST)
        if formaUser.is_valid():
            formaUser.save()
            return redirect('index')
    else:
        formaUser = Userform()
    
    return render(request, 'agregar.html', {'formaUser':formaUser})

def Editar(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        formaUser = Userform(request.POST, instance=user)
        if formaUser.is_valid():
            formaUser.save()
            return redirect('index')
    else:
        formaUser = Userform(instance=user)
    
    return render(request, 'editar.html', {'formaUser':formaUser})

def Eliminar(request, id):
    user = get_object_or_404(User, pk=id)
    if user:
        user.delete()
    return redirect('index')
    