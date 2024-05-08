from rest_framework import serializers
from .models import Tag, Place


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            "id",
            "title",
            "rating",
            "description",
            "location",
            "mainImage",
            "reviewNumber",
            "userID",
        )
