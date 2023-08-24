from django.shortcuts import render
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from store.models import Customer, Product


def say_hello(request):
    discounted_price = ExpressionWrapper(
        F("unit_price") * 0.8, output_field=DecimalField()
    )

    queryset = Product.objects.annotate(discounted_price=discounted_price)

    return render(request, "hello.html", {"name": "Devdhar", "result": list(queryset)})
