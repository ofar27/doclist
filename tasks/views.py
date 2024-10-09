from django.http import HttpResponse
from django.shortcuts import render, redirect
from tasks.models import Collection

# Create your views here.
def index(request):
    context = {}
    context["collections"] = Collection.objects.order_by("name")
    return render(request, 'tasks/index.html', context)

def add_collection(request):
    if request.method == "POST":
        collection_name = request.POST.get("collection-name")
        if collection_name:  # Vérifie si le nom n'est pas vide
            Collection.objects.create(name=collection_name)
    return redirect('home')
