from django.urls import path
from . import views

urlpatterns = [
    # TODO Remover
    path("hello-world/", views.hello_world, name="hello_world"),
    path("getOfenseWords/", views.getOfenseWords, name="getOfenseWords"),
    path(
        "<int:place_id>/favorite",
        views.favoritePlace,
        name="favoritePlace",
    ),
    path("<int:place_id>/getBestTags", views.getBestTags, name="getBestTags"),
    path("tags", views.getTags, name="getTags"),
    path("<int:tag_id>/operationTag", views.oprationTag, name="operationTag"),
    path("getPlaces", views.getPlaces, name="getPlaces"),
    path("<int:place_id>/operationPlace", views.operationPlace, name="operationPlace"),
]
