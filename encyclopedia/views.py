from django.shortcuts import render

from django.http import HttpResponse

from markdown2 import markdown

from random import shuffle

from . import util

renderHTML = 'encyclopedia/load.html'
loadHTML = 'encyclopedia/templates/encyclopedia/load.html'

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    return render(request, "encyclopedia/create.html", {
        
    })

def load_page(request, title):
    string = '{% extends "encyclopedia/layout.html" %}{% block title %}' + \
                title + '{% endblock %}{% block body %}' + markdown(util.get_entry(title)) + '{% endblock %}'
    file = open("encyclopedia/templates/encyclopedia/load.html", "w")
    file.write(string)
    file.close()
    return render(request, "encyclopedia/load.html")

def random(request):
    entries = util.list_entries()
    shuffle(entries)
    return load_page(request, entries[0])

def title(request, title):
    string = util.get_entry(title)
    if string == None:
        return render(request, "encyclopedia/error.html")
    else:
        return load_page(request, title)




