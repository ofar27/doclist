from http.client import HTTPResponse
from xml.sax.saxutils import escape

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.utils.html import escape

from tasks.models import Collection

# Create your views here.
def index(request):
    context = {}
    context["collections"] = Collection.objects.order_by("name")
    return render(request, 'tasks/index.html', context)

def add_collection(request):
    if request.method == "POST":
        collection_name = escape(request.POST.get("collection-name"))
        if collection_name:  # Vérifie si le nom n'est pas vide
            collection, created = Collection.objects.get_or_create(name=collection_name)
            if not created:
                return HttpResponse("La colletion existe déjà.")

    return redirect('home')
