from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from markdown2 import markdown

from random import shuffle, randrange

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Entry Name")
    content = forms.CharField(widget=forms.Textarea, label="")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html", {
            "form": NewEntryForm()
        })
    elif request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                return render(request, "encyclopedia/error.html")
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("title", kwargs={"title": title}))


def random(request):
    entries = util.list_entries()
    x = randrange(0,len(entries))
    # return page(request, entries[x])
    return HttpResponseRedirect(reverse("title", kwargs={"title": entries[x]}))

def title(request, title):
    string = util.get_entry(title)
    if string == None:
        return render(request, "encyclopedia/error.html")
    else:
        string = '{% extends "encyclopedia/layout.html" %}{% block title %}' + \
                title + '{% endblock %}{% block body %}' + markdown(util.get_entry(title)) + '{% endblock %}'
        file = open("encyclopedia/templates/encyclopedia/load.html", "w")
        file.write(string)
        file.close()
        return render(request, "encyclopedia/load.html")




