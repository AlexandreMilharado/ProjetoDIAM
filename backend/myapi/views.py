from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.shortcuts import get_object_or_404
from myapi.models import Place, Tag
from .serializers import *
from rest_framework import status


# TODO Mudar bixo
@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(["GET"])
def getOfenseWords(request):
    return Response({"message": searchOfensiveWords()})


@api_view(["GET", "POST"])
def favoritePlace(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    match request.method:
        case "GET":
            return Response({"result": place.isFavoritePlace(request.user)})

        case "POST":
            if not request.user.is_authenticated:
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
    serializer = TagSerializer(Tag.objects.all(), many=True)
    return Response({"result": serializer.data})


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
