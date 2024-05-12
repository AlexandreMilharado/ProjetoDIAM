from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.shortcuts import get_object_or_404
from myapi.models import Place, Tag
from .serializers import *
from rest_framework import status
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


# TODO Mudar bixo
@api_view(["GET"])
def hello_world(request):
    get_object_or_404(Place, pk=1).delete()

    return Response({"message": "Hello, world!"})


@api_view(["GET"])
def getOfenseWords(request):
    return Response({"message": searchOfensiveWords()})


@api_view(["GET", "POST"])
def favoritePlace(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    match request.method:
        case "GET":
            user = request.user
            if not user.is_authenticated and request.META.get("HTTP_AUTHORIZATION"):
                try:
                    token = Token.objects.get(key=request.META.get("HTTP_AUTHORIZATION").split(" ")[1])
                    user = token.user
                except Token.DoesNotExist:
                    pass
            return Response({"result": place.isFavoritePlace(user)})

        case "POST":

            if not request.user.is_authenticated:
                if request.META.get("HTTP_AUTHORIZATION"):
                    try:
                        token = Token.objects.get(
                            key=request.META.get("HTTP_AUTHORIZATION").split(" ")[1]
                        )
                    except Token.DoesNotExist:
                        return Response(
                            {"error": "Token not found"},
                            status=status.HTTP_401_UNAUTHORIZED,
                        )
                    place.favoriteOrUnFavoritePlace(token.user.utilizador)
                    return Response(
                        {"result": place.isFavoritePlace(token.user.utilizador)}
                    )
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data="Faça login para guardar favoritos!",
                )

            place.favoriteOrUnFavoritePlace(request.user.utilizador)
            return Response({"result": place.isFavoritePlace(request.user)})

        case _:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getTags(request):
    place = request.query_params.get("place")
    if place is not None:
        serializer = TagSerializer(
            Tag.objects.filter(tagplace__placeID=place), many=True
        )
    else:
        serializer = TagSerializer(Tag.objects.all(), many=True)
    return Response({"result": serializer.data})


@api_view(["DELETE", "POST"])
def oprationTag(request, tag_id):
    if not request.user.is_superuser:
        return Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data="Não tem permissiões para executar operação",
        )

    tag = get_object_or_404(Tag, pk=tag_id)
    match request.method:
        case "DELETE":
            tag.delete()
            return Response(status=status.HTTP_200_OK)

        case "POST":
            try:
                tag.name = request.POST["name"]
                tag.save()
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_200_OK)

        case _:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getPlaces(request):
    search = request.query_params.get("search")
    cachedNumber = request.query_params.get("cachedNumber")
    mode = request.query_params.get("mode")
    try:
        cachedNumber = 0 if cachedNumber is None else int(cachedNumber)
        mode = "" if mode is None else mode
    except ValueError:
        cachedNumber = 0

    places = searchPlace(searchPlacePreviousMode(mode, request.user), search)

    if places is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    places = places.order_by("-rating").order_by("-id")[
        cachedNumber : (cachedNumber + 10)
    ]

    serializer = PlaceSerializer(places, many=True)
    return Response({"result": serializer.data})

@api_view(["GET"])
def getPlace(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    serializer = PlaceSerializer(place)
    return Response({"place":serializer.data}) 

@api_view(["GET"])
def getBestTags(request, place_id):
    limit = request.query_params.get("limit")
    place = get_object_or_404(Place, pk=place_id)
    tags = (
        Tag.objects.filter(tagplace__placeID=place)
        .annotate(num_likes=Count("tagplace__likeNumber"))
        .order_by("-num_likes")
    )
    tags = tags if limit is None else tags[: int(limit)]
    serializer = TagSerializer(
        tags,
        many=True,
    )
    return Response({"result": serializer.data})


@api_view(["POST", "DELETE"])
def operationPlace(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    match request.method:
        case "DELETE":
            place.delete()
            return Response(status=status.HTTP_200_OK)
        case "POST":
            try:
                place.name = request.POST["name"]
                place.save()
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_200_OK)

        case _:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response(
                {"error": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST
            )


# Filter Language Functions
def searchOfensiveWords():
    return transformHtmlToText(
        "https://raw.githubusercontent.com/dunossauro/chat-detox/main/palavras.txt"
    )


# Parsing HTML Functions
def transformHtmlToText(URL):
    return requests.get(
        URL,
    ).text


# Search Places Functions
def searchPlace(places, search):
    if search == "" or search is None:
        return places

    tokens = search.split(":")
    if len(tokens) == 1:
        return places.filter(title__contains=tokens[0])

    match tokens[0].upper():
        case "TITLE":
            return places.filter(title__contains=tokens[1])

        case "RATING":
            return places.filter(rating__contains=tokens[1])

        case "LOCATION":
            return places.filter(location__contains=tokens[1])

        case "TAG":
            try:
                return places.filter(
                    tagplace__tagID=get_object_or_404(Tag, name=tokens[1])
                )
            except Tag.DoesNotExist:
                return []

        case _:
            return None


def searchPlacePreviousMode(search, user):
    if search == "" or search is None:
        return Place.objects.all()

    match search.upper():
        case "FAVORITE":
            return Place.objects.filter(favoritePlaces=user.utilizador)

        case "MYPLACES":
            return Place.objects.filter(userID=user.id)

        case _:
            return Place.objects.all()
