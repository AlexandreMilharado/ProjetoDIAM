from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from myapi.models import Utilizador, Place
from django.utils.dateparse import parse_datetime


def index(request):
    places = [Place(title='Place de test atrás da cozinha da casa da tia do meu pai mais belho',rating=4,
                    description='Descrição do sitio de teste ao pé da cidade Teste Da santa teste',
                    location='ISCTE', reviewNumber=3), 
                    Place(title='Place de test',rating=9,
                    description='Descrição do sitio de teste ao pé da cidade Teste Da santa teste',
                    location='ISCTE', reviewNumber=3),
                    Place(title='Place de test',rating=7,
                    description='Descrição do sitio de teste ao pé da cidade Teste Da santa teste',
                    location='ISCTE', reviewNumber=3),
                    Place(title='Place de test',rating=9,
                    description='Descrição do sitio de teste ao pé da cidade Teste Da santa teste',
                    location='ISCTE', reviewNumber=3),
                    Place(title='Place de test',rating=7,
                    description='Descrição do sitio de teste ao pé da cidade Teste Da santa teste',
                    location='ISCTE', reviewNumber=3),
                    Place(title='Place de test',rating=9,
                    description='Descrição do sitio de teste ao pé da cidade Teste Da santa teste',
                    location='ISCTE', reviewNumber=3),
                    Place(title='Place de test',rating=7,
                    description='Descrição do sitio de teste ao pé da cidade Teste Da santa teste',
                    location='ISCTE', reviewNumber=3),
                    Place(title='Place de test',rating=2,
                    description='Descrição do sitio de teste ao pé da cidade Teste Da santa teste',
                    location='ISCTE', reviewNumber=3)]
    
    return render(request, 'website/index.html',{'placeList':places})

def loginView(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return render(request, 'website/login.html')
        if username and password:
            user = authenticate(username= username,password=password)
            if user is not None:
                login(request, user)
                request.session['votos'] = 0
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'website/login.html',{'error_message':'Credenciais incorretas'})
        else:
            return HttpResponseRedirect(reverse('website:login'))

    else:
        return render(request, 'website/login.html')

def registar(request):
    if request.method == 'POST':
        try:
            username=  request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            birthday = request.POST['birthday']
        except KeyError:
            return render(request, 'website/registar.html')
        if username and password and email:
            aluno = Utilizador(user=User.objects.create_user(username, email, password),birthday=parse_datetime(birthday))
            aluno.save()

            return HttpResponseRedirect(reverse('website:login'))
        else:
            return HttpResponseRedirect(reverse('website:registar'))

    else:
        return render(request, 'website/registar.html')
    
def profile(request):
    if request.user.is_authenticated:
        utilizador = Utilizador.objects.get(user=request.user)
        return render(request, "website/profile.html",{'user' : utilizador})
    else:
       return HttpResponseRedirect(reverse('website:login'))
