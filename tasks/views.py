from http.client import HTTPResponse
from xml.sax.saxutils import escape

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import escape
from django.utils.text import slugify

from tasks.models import Collection, Task


def index(request):
    context = {}

    collection_slug = request.GET.get("collection")
    collection = Collection.get_default_collection()

    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)

    context["collections"] = Collection.objects.order_by("slug") # le "-" pour l'ordre alphabétique
    context["collection"] = collection
    context["tasks"]  = collection.task_set.order_by("description")


    return render(request, 'tasks/index.html', context=context)


def add_collection(request):
    if request.method == "POST":
        collection_name = escape(request.POST.get("collection-name"))
        if collection_name:  # Vérifie si le nom n'est pas vide
            collection, created = Collection.objects.get_or_create(name=collection_name, slug=slugify(collection_name))
            if not created:
                return HttpResponse("La colletion existe déjà.", status=409)

            return HttpResponse(f'<h2>{collection_name}</h2>')


def add_task(request):
    collection_slug = request.POST.get("collection")
    collection = get_object_or_404(Collection, slug=collection_slug)
    description = escape(request.POST.get("task-description"))
    Task.objects.create(description=description, collection=collection)

    return HttpResponse(description)



def get_tasks(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    tasks = collection.task_set.order_by("description")

    return render(request, 'tasks/tasks.html', context={"tasks":tasks})

