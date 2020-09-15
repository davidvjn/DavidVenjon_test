from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db import connection

# @todo
# connexion avec la bdd


data = [
    {
        "firstname": "John",
        "name": "Doe",
        "img": "none",
        "description": "Bonjour je suis 1"
    },
    {
        "firstname": "John",
        "name": "Doe",
        "img": "none",
        "description": "Bonjour je suis 2"
    },
    {
        "firstname": "John",
        "name": "Doe",
        "img": "none",
        "description": "Bonjour je suis 3"
    }
]

PopStars = "Profile Stars"

def index(request):
    return HttpResponse(render_to_string('index.html', {'stars': PopStars, 'data': data}))
