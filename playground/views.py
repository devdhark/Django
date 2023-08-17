from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.db.models.aggregates import Count, Max, Min, Sum
from django.db.models.functions import Concat
from store.models import Collection, Customer, OrderItem, Product


def say_hello(request):
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    )

    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Concat("first_name", Value(" "), "last_name")
    )

    return render(request, "hello.html", {"name": "Devdhar", "result": list(queryset)})
