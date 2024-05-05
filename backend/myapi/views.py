from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.shortcuts import get_object_or_404
from myapi.models import Place


# TODO Mudar bixo
@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(["GET"])
def getOfenseWords(request):
    return Response({"message": searchOfensiveWords()})


@api_view(["GET"])
def isFavoritePlace(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return Response({"result": place.isFavoritePlace(request.user)})


def searchOfensiveWords():
    return transformHtmlToText(
        "https://raw.githubusercontent.com/dunossauro/chat-detox/main/palavras.txt"
    )


def transformHtmlToText(URL):
    return requests.get(
        URL,
    ).text
