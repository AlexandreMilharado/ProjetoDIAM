from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Tag(models.Model):
    name = models.CharField(max_length=50)


class Utilizador(models.Model):
    birthday = models.DateField()
    profileImage = models.ImageField(default="")
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Place(models.Model):
    title = models.CharField(max_length=50)
    rating = models.SmallIntegerField(null=True)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    mainImage = models.ImageField(default="")
    reviewNumber = models.IntegerField(default=0)
    userID = models.ForeignKey(Utilizador, null=True, on_delete=models.SET_NULL)
    favoritePlaces = models.ManyToManyField(Utilizador, related_name="favoritePlaces")


class Review(models.Model):
    comment = models.CharField(max_length=300, null=True)
    rating = models.SmallIntegerField(null=True)
    mainImage = models.ImageField(default="")
    data = models.DateField(default=timezone.now())
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    userID = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    reviewID = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    likedTags = models.ManyToManyField(Tag, related_name="likedTags")


class TagPlace(models.Model):
    likeNumber = models.IntegerField(default=1)
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    tagID = models.ForeignKey(Tag, on_delete=models.CASCADE)
