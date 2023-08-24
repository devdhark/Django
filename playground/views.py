from django.shortcuts import render
from django.db.models import (
    Q,
    F,
    Value,
    Func,
    Count,
    ExpressionWrapper,
    DecimalField,
    Max,
)
from store.models import Collection, Customer, Product


def say_hello(request):
    queryset = Collection.objects.annotate(count=Count("product__id"))

    return render(request, "hello.html", {"name": "Devdhar", "result": list(queryset)})
