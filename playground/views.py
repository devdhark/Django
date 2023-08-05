from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Collection, Customer, OrderItem, Product


def say_hello(request):
    queryset = OrderItem.objects.filter(product__collection__id=True)

    return render(
        request, "hello.html", {"name": "Devdhar", "orderitems": list(queryset)}
    )
