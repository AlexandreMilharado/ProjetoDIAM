from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


# TODO Mudar bixo
@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(["GET"])
def getOfenseWords(request):
    return Response({"message": searchOfensiveWords()})


def searchOfensiveWords():
    return transformHtmlToText(
        "https://raw.githubusercontent.com/dunossauro/chat-detox/main/palavras.txt"
    )


def transformHtmlToText(URL):
    return requests.get(
        URL,
    ).text
