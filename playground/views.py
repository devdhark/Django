from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Collection, Order, OrderItem, Product
from tags.models import TaggedItem


@transaction.atomic()
def say_hello(request):
    queryset = Product.objects.raw("SELECT * FROM store_product")

    return render(request, "hello.html", {"name": "Devdhar", "result": list(queryset)})
