from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from myapi.models import Utilizador
from django.utils.dateparse import parse_datetime


def index(request):
    return render(request, 'backend/index.html')

def loginView(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return render(request, 'backend/login.html')
        if username and password:
            user = authenticate(username= username,password=password)
            if user is not None:
                login(request, user)
                request.session['votos'] = 0
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'backend/login.html',{'error_message':'Credenciais incorretas'})
        else:
            return HttpResponseRedirect(reverse('login'))

    else:
        return render(request, 'backend/login.html')

def registar(request):
    if request.method == 'POST':
        try:
            username=  request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            birthday = request.POST['birthday']
        except KeyError:
            return render(request, 'backend/registar.html')
        if username and password and email:
            aluno = Utilizador(user=User.objects.create_user(username, email, password),birthday=parse_datetime(birthday))
            aluno.save()

            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('registar'))

    else:
        return render(request, 'backend/registar.html')