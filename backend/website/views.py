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
from myapi.views import searchOfensiveWords
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


def index(request):
    placeList = Place.objects.all()  # TODO Buscar os melhores
    return render(
        request,
        "website/index.html",
        {"placeList": placeList, "emptyPlaces": "Sem lugares? Crie um!"},
    )


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
    context = {}
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        location = request.POST["location"]
        try:
            mainImage = request.FILES["image"]
        except KeyError:
            mainImage = None

        if (
            isTextOfensive(title)
            or isTextOfensive(location)
            or isTextOfensive(description)
        ):
            context["modalMessage"] = {
                "msg": "Texto previamente inserido é potencialmente ofensivo",
                "image": "/images/censorship.svg",
            }
        else:
            p = Place(
                title=title,
                description=description,
                location=location,
                mainImage=saveAndGetImage(mainImage, request.user, "defaultPlace.jpg"),
                userID=request.user.utilizador,
            )
            p.save()

    placeList = Place.objects.filter(userID=request.user.id)
    context["placeList"] = placeList
    context["emptyPlaces"] = "Sem lugares? Crie um!"
    return render(request, "website/myPlaces.html", context)


@login_required(login_url="/login")
def favoritePlaces(request):
    placeList = Place.objects.filter(favoritePlaces=request.user.utilizador)
    return render(
        request,
        "website/genericPage.html",
        {"placeList": placeList, "emptyPlaces": "Sem lugares? Adicione um!"},
    )


@login_required(login_url="/login")
def favoriteOrUnFavoritePlace(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.favoriteOrUnFavoritePlace(request.user.utilizador)
    return redirect(request.META.get("HTTP_REFERER", "http://127.0.0.1:8000/"))


# File Functions
def saveAndGetImage(file, user, defaultFile):
    if not file:
        return f"/images/{defaultFile}"

    fs = FileSystemStorage()
    filename = fs.save(
        f"{user.id}/{datetime.datetime.now().timestamp()}.{getExtension(file)}", file
    )
    return f"/media{fs.url(filename)}"


def getExtension(file):
    return file.name.split(".")[-1]


def isTextOfensive(text):
    textToFind = text.lower()
    bannedWords = searchOfensiveWords().split("\n")
    for word in bannedWords:
        if word in textToFind and word and textToFind:
            return True
    return False
