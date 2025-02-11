"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("login", views.loginView, name="login"),
    path("registar", views.registar, name="registar"),
    path("logout", views.logoutView, name="logout"),
    path("myPlaces", views.myPlaces, name="myPlaces"),
    path("favoritePlaces", views.favoritePlaces, name="favoritePlaces"),
    path("createTag", views.createTag, name="createTag"),
    path("<int:place_id>/detalhe", views.detalhePlace, name="detalhe"),
    path("<int:place_id>/editPlace", views.editarPlace, name="editarPlace"),
    path("<int:place_id>/criarReview", views.criarReview, name="criarReview"),
]
