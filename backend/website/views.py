from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from myapi.models import Utilizador, Place, Tag, TagPlace,Review
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.storage import FileSystemStorage
import datetime
from myapi.views import searchOfensiveWords
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone


# Test decorators
def isSuperUser(user):
    return user.is_superuser


# Views
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
                request.session["votos"] = 0  # TODO Retirar e meter outra coisa
                reverseTo = request.environ["HTTP_REFERER"].split("=")
                firstTimeLoginSuperUser(user)
                return HttpResponseRedirect(
                    reverse(
                        f"website:{'index' if len(reverseTo) == 1 else reverseTo[1][1:]}"
                    )
                )
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
            addTagsToPlace(request, p)

    context["placeList"] = Place.objects.filter(userID=request.user.id)
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


@user_passes_test(test_func=isSuperUser, login_url="/login")
def createTag(request):
    if request.method == "POST":
        try:
            tagName = request.POST["tagName"]
            t = Tag(name=tagName)
            t.save()
        except KeyError:
            return render(
                request,
                "website/createTag.html",
                {
                    "modalMessage": {
                        "msg": "Erro ao criar a Tag",
                        "image": "/images/errorInput.svg",
                    }
                },
            )

    tags = Tag.objects.all().order_by("-id")
    return render(request, "website/createTag.html", {"tags": tags})


def detalhePlace(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    tags = TagPlace.objects.filter(placeID=place).order_by("-likeNumber")[:15]
    reviews = Review.objects.filter(placeID=place)
    return render(request, "website/detalhe.html", 
                  {"place": place, "isFavorite": place.isFavoritePlace(request.user), "tags":tags,"reviews":reviews})


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


# SuperUser Functions
def firstTimeLoginSuperUser(user):
    if user.is_superuser:
        try:
            Utilizador.objects.get(user=user)
        except Utilizador.DoesNotExist:
            u = Utilizador(
                user=user,
                birthday=timezone.now(),
            )
            u.save()


# Utils
def addTagsToPlace(request, place):
    tagsID = []
    try:
        for i in range(Tag.objects.all().count()):
            if request.POST[f"tag-{i}"] != "None":
                tagsID.append(request.POST[f"tag-{i}"])
    except KeyError:
        pass

    uniqueTagsID = set(tagsID)

    for tagID in uniqueTagsID:
        t = TagPlace(placeID=place, tagID=get_object_or_404(Tag, id=tagID))
        t.save()
