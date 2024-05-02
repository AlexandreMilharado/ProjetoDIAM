from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from myapi.models import Utilizador, Place
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.storage import FileSystemStorage
import datetime


def index(request):
    placeList = Place.objects.all()  # TODO Buscar os melhores
    return render(request, "website/index.html", {"placeList": placeList})


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


@login_required(login_url="/login")
def profile(request):
    utilizador = Utilizador.objects.get(user=request.user)
    return render(request, "website/profile.html", {"user": utilizador})


def logoutView(request):
    request.session.flush()
    logout(request)
    return HttpResponseRedirect(reverse("website:index"))


@login_required(login_url="/login")
def myPlaces(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        location = request.POST["location"]
        try:
            mainImage = request.FILES["image"]
        except KeyError:
            mainImage = None
        if title and location:
            p = Place(
                title=title,
                description=description,
                location=location,
                mainImage=saveAndGetImage(mainImage, request.user, "defaultPlace.jpg"),
                userID=request.user.utilizador,
            )
            p.save()
    placeList = Place.objects.filter(userID=request.user.id)
    return render(request, "website/myPlaces.html", {"placeList": placeList})


def saveAndGetImage(file, user, defaultFile):
    if not file:
        return f"/images/{defaultFile}"

    fs = FileSystemStorage()
    filename = fs.save(
        f"{user.id}/{datetime.datetime.now().timestamp()}.{getExtension(file)}", file
    )
    fs
    print(filename)
    return f"/media{fs.url(filename)}"


def getExtension(file):
    return file.name.split(".")[-1]