from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Collection, Customer, OrderItem, Product


def say_hello(request):
    queryset = Product.objects.filter(inventory=F("collection__id"))

    return render(
        request, "hello.html", {"name": "Devdhar", "products": list(queryset)}
    )
