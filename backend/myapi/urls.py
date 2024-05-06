from django.urls import path
from . import views

urlpatterns = [
    # TODO Remover
    path("hello-world/", views.hello_world, name="hello_world"),
    path("getOfenseWords/", views.getOfenseWords, name="getOfenseWords"),
    path(
        "<int:place_id>/isFavorite",
        views.isFavoritePlace,
        name="isFavoritePlace",
    ),
    path("tags", views.getTags, name="getTags"),
]
