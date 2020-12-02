from django.shortcuts import render, redirect
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
            "entries": util.list_entries(),
            "heading": 'All Pages'
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
            for entry in util.list_entries():
                if title.lower() == entry.lower():
                    return HttpResponseRedirect(reverse("pagealreadyexists"))
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("title", kwargs={"title": title}))


def random(request):
    entries = util.list_entries()
    x = randrange(0,len(entries))
    # return page(request, entries[x])
    return HttpResponseRedirect(reverse("title", kwargs={"title": entries[x]}))

def edit(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": util.get_entry(title)
        })
    elif request.method == "POST":
        util.save_entry(title, request.POST['edited_content'])
        return HttpResponseRedirect(reverse("title", kwargs={"title": title}))

def title(request, title):
    string = util.get_entry(title)
    if string == None:
        return HttpResponseRedirect(reverse('pagenotfound'))
    else:
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "content": markdown(util.get_entry(title))
        })

def search(request):
    query = request.GET['q']
    entries = []
    for entry in util.list_entries():
        if query.lower() == entry.lower():
            return HttpResponseRedirect(reverse("title", kwargs={"title": entry}))
        elif query.lower() in entry.lower():
            entries.append(entry)
    if entries == []:
        return HttpResponseRedirect(reverse('pagenotfound'))
    else:
        return render(request, "encyclopedia/index.html", {
            "heading": f"Search results for '{query}'",
            "entries": entries
        })

def pagenotfound(request):
    return render(request, "encyclopedia/pagenotfound.html")

def pagealreadyexists(request):
    return render(request, "encyclopedia/pagealreadyexists.html")






