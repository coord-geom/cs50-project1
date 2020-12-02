from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("random", views.random, name="random"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>", views.title, name="title"),
    path("pagenotfound", views.pagenotfound, name="pagenotfound"),
    path("pagealreadyexists", views.pagealreadyexists, name="pagealreadyexists")
]
