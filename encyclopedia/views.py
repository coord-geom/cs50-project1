from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def css(request):
    return render(request, "encyclopedia/css.html", {
        "entries": util.list_entries()
    })

def django(request):
    return render(request, "encyclopedia/django.html", {
        "entries": util.list_entries()
    })

def git(request):
    return render(request, "encyclopedia/git.html", {
        "entries": util.list_entries()
    })

def html(request):
    return render(request, "encyclopedia/html.html", {
        "entries": util.list_entries()
    })

def python(request):
    return render(request, "encyclopedia/python.html", {
        "entries": util.list_entries()
    })



