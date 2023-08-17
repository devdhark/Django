from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Max, Min, Sum
from store.models import Collection, Customer, OrderItem, Product


def say_hello(request):
    queryset = Customer.objects.annotate(new_id=F("id"))

    return render(request, "hello.html", {"name": "Devdhar", "result": list(queryset)})
