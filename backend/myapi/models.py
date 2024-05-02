from django.db import models
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Utilizador(models.Model):
    birthday = models.DateField()
    profileImage = models.ImageField(default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Place(models.Model):
    title = models.CharField(max_length=50)
    rating = models.SmallIntegerField(null=True)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    mainImage = models.ImageField(default="")
    reviewNumber = models.IntegerField(default=0)
    userID = models.ForeignKey(Utilizador, null=True, on_delete=models.SET_NULL)
    favoritePlaces = models.ManyToManyField(Utilizador, related_name="favoritePlaces")

    def getRatingRange(self):
        return range(self.rating // 2)

    def hasOddRating(self):
        return self.rating % 2 == 1

    def __str__(self):
        return self.title

    def bestRatedTags(self):
        top_tags = (
            Tag.objects.filter(tagplace__placeID=self)
            .annotate(num_likes=Count("tagplace__likeNumber"))
            .order_by("-num_likes")[:3]
        )
        return [tag.name for tag in top_tags]


class Review(models.Model):
    comment = models.CharField(max_length=300, null=True)
    rating = models.SmallIntegerField(null=True)
    mainImage = models.ImageField(default="")
    data = models.DateField(default=timezone.now())
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    userID = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    reviewID = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    likedTags = models.ManyToManyField(Tag, related_name="likedTags")

    def __str__(self):
        return f"{Place.objects.get(pk=self.placeID)} {self.pk}"


class TagPlace(models.Model):
    likeNumber = models.IntegerField(default=1)
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    tagID = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"Place {self.placeID} - Tag: {self.tagID}"


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Utilizador(models.Model):
    birthday = models.DateField()
    profileImage = models.ImageField(default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Place(models.Model):
    title = models.CharField(max_length=50)
    rating = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    mainImage = models.ImageField(default="")
    reviewNumber = models.IntegerField(default=0)
    userID = models.ForeignKey(Utilizador, null=True, on_delete=models.SET_NULL)
    favoritePlaces = models.ManyToManyField(Utilizador, related_name="favoritePlaces")

    def getRatingRange(self):
        return range(self.rating // 2)

    def hasOddRating(self):
        return self.rating % 2 == 1


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
