from django.shortcuts import render
from .models import Product, OrderProduct
from django.http import HttpResponse


# Create your views here.
def ticket_promedio():
    order_products = OrderProduct.objects.all()
    orders = {}
    for order_product in order_products:
        products_of_order = order_product.product_id
        orders[order_product.order_id] = orders.get(
            order_product.order_id, 0) + order_product.quantity*products_of_order.price

    promedio = sum(orders.values())/len(orders)

    return promedio


def indicadores(request):  # retornahttpresponse
