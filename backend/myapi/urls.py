from django.urls import path
from . import views

urlpatterns = [
    # TODO Remover
    path("hello-world/", views.hello_world, name="hello_world"),
    path("getOfenseWords/", views.getOfenseWords, name="getOfenseWords"),
]
