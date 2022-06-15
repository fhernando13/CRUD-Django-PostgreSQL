from smtplib import SMTPResponseException
from django.shortcuts import render
from django.http import HttpResponse
from testuser.models import User

# Create your views here.

def bienvenido(request):
    no_users = User.objects.count()
    #users = User.objects.all()
    users = User.objects.order_by('id')
    return render(request, 'index.html', {'no_users':no_users, 'users':users})