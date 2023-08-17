from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Sum
from store.models import Collection, Customer, OrderItem, Product


def say_hello(request):
    result = Product.objects.aggregate(count=Count("id"), min_price=Min("unit_price"))

    return render(request, "hello.html", {"name": "Devdhar", "result": result})
