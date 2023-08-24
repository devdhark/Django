from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


def say_hello(request):
    return render(request, "hello.html", {"name": "Devdhar"})
