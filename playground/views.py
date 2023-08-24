from django.shortcuts import render
from django.db.models import Q, F, Value, Func, Count
from store.models import Customer, Product


def say_hello(request):
    queryset = Customer.objects.annotate(orders_count=Count("order"))

    return render(request, "hello.html", {"name": "Devdhar", "result": list(queryset)})
