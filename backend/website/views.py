from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from myapi.models import Utilizador, Place
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import login_required, user_passes_test



def index(request):
    places = Place.objects.all()
    return render(request, "website/index.html", {"placeList": places})


def loginView(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
        except KeyError:
            return render(request, "website/login.html")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session["votos"] = 0
                return HttpResponseRedirect(reverse("website:index"))
            else:
                return render(
                    request,
                    "website/login.html",
                    {"error_message": "Credenciais incorretas"},
                )
        else:
            return HttpResponseRedirect(reverse("website:login"))

    else:
        return render(request, "website/login.html")


def registar(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            birthday = request.POST["birthday"]
        except KeyError:
            return render(request, "website/registar.html")
        if username and password and email:
            aluno = Utilizador(
                user=User.objects.create_user(username, email, password),
                birthday=parse_datetime(birthday),
            )
            aluno.save()

            return HttpResponseRedirect(reverse("website:login"))
        else:
            return HttpResponseRedirect(reverse("website:registar"))

    else:
        return render(request, "website/registar.html")


@login_required(login_url="/website/login")
def profile(request):
    if request.user.is_authenticated:
        utilizador = Utilizador.objects.get(user=request.user)
        return render(request, "website/profile.html", {"user": utilizador})
    else:
        return HttpResponseRedirect(reverse("website:login"))


def logoutView(request):
    request.session.flush()
    logout(request)
    return HttpResponseRedirect(reverse("website:index"))
