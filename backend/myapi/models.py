from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Explorer(models.Model):
    birthday = models.DateField()
    profileImage = models.ImageField(default="")


class Place(models.Model):
    title = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    mainImage = models.ImageField(default="")
    tags = models.ManyToManyField(Tag, related_name="places")
    userID = models.ForeignKey(Explorer, null=True, on_delete=models.SET_NULL)
    favoritePlaces = models.ManyToManyField(Explorer, related_name="favoritePlaces")


class Post(models.Model):
    title = models.CharField(max_length=50)
    mainImage = models.ImageField(default="")
    numLikes = models.IntegerField(default=0)
    numDisLikes = models.IntegerField(default=0)
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    userID = models.ForeignKey(Explorer, on_delete=models.CASCADE)


class Comment(models.Model):
    message = models.CharField(max_length=300)
    numLikes = models.IntegerField(default=0)
    numDisLikes = models.IntegerField(default=0)
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)


class Reaction(models.Model):
    userID = models.ForeignKey(Explorer, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    like = models.BooleanField(null=True)
    commentID = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)
    postID = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    placeID = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
