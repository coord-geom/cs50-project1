from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("random", views.random, name="random"),
    path("wiki/<str:title>", views.title, name="title")
    #path("wiki/CSS", views.CSS, name="CSS"),
    #path("wiki/Django", views.Django, name="Django"),
    #path("wiki/Git", views.Git, name="Git"),
    #path("wiki/HTML", views.HTML, name="HTML"),
    #path("wiki/Python", views.Python, name="Python"),  
]
