from django.db import models
from django.utils import timezone
from django.db.models import Count, Sum
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
    rating = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    mainImage = models.ImageField(default="")
    reviewNumber = models.IntegerField(default=0)
    userID = models.ForeignKey(Utilizador, null=True, on_delete=models.SET_NULL)
    favoritePlaces = models.ManyToManyField(Utilizador, related_name="favoritePlaces")

    def updateRating(self):
        reviews = Review.objects.filter(placeID=self)
        self.rating = reviews.aggregate(total_rating=Sum("rating"))[
            "total_rating"
        ] / len(reviews)
        self.save()

    def getRatingRange(self):
        return range(self.rating // 2)

    def hasOddRating(self):
        return self.rating % 2 == 1

    def getRatingColor(self):
        if self.rating < 4:
            return "#cd2e2e"
        if self.rating < 7:
            return "#e7bd3f"
        else:
            return "#089638"

    def halfRating(self):
        return self.rating / 2

    def __str__(self):
        return self.title

    def bestRatedTags(self):
        top_tags = (
            Tag.objects.filter(tagplace__placeID=self)
            .annotate(num_likes=Count("tagplace__likeNumber"))
            .order_by("-num_likes")[:3]
        )
        return [tag.name for tag in top_tags]

    def isFavoritePlace(self, utilizador):
        return self.favoritePlaces.filter(id=utilizador.id).exists()

    def favoriteOrUnFavoritePlace(self, utilizador):
        if self.isFavoritePlace(utilizador):
            self.favoritePlaces.remove(utilizador)
        else:
            self.favoritePlaces.add(utilizador)


class Review(models.Model):
    comment = models.CharField(max_length=300, null=True)
    rating = models.SmallIntegerField(null=True)
    data = models.DateField(default=timezone.now)
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    userID = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    likedTags = models.ManyToManyField(Tag, related_name="likedTags")

    def __str__(self):
        return f"{self.placeID} {self.pk}"

    def getRatingRange(self):
        return range(self.rating // 2)

    def hasOddRating(self):
        return self.rating % 2 == 1


class TagPlace(models.Model):
    likeNumber = models.IntegerField(default=1)
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    tagID = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"Place {self.placeID} - Tag: {self.tagID}"
