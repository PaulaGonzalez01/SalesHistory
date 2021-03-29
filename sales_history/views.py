from django.shortcuts import render
from .models import Product, OrderProduct, Department
from django.http import HttpResponse
import heapq
from operator import itemgetter


# server functions
def ticket_promedio():
    order_products = OrderProduct.objects.all()
    orders = {}
    for order_product in order_products:
        product_of_order = order_product.product_id
        orders[order_product.order_id] = orders.get(
            order_product.order_id, 0) + order_product.quantity*product_of_order.price

    promedio = sum(orders.values())/len(orders)

    return promedio


def margen_promedio():
    order_products = OrderProduct.objects.all()
    orders = {}
    for order_product in order_products:
        product_of_order = order_product.product_id
        orders[order_product.order_id] = orders.get(
            order_product.order_id, 0) + product_of_order.margin

    promedio = sum(orders.values())/len(orders)

    return promedio


def cantidad_promedio():
    order_products = OrderProduct.objects.all()
    orders = {}
    for order_product in order_products:
        product_of_order = order_product.product_id
        orders[order_product.order_id] = orders.get(
            order_product.order_id, 0) + order_product.quantity

    promedio = sum(orders.values())/len(orders)

    return promedio


def get_ganancia_producto(pquantity, price, margin):
    return quantity*price*margin


def dic_productos_departamentos():
    order_products = OrderProduct.objects.all()
    departments_with_products = {}

    for order_product in order_products:
        product_of_order = order_product.product_id
        product_department = product_of_order.department_id
        dic_products = departments_with_products.get(
            product_department.department, {})

        dic_products[order_product.product_id] = dic_products.get(
            order_product.product_id, 0) + order_product.quantity

        departments_with_products[product_of_order] = dic_products

    for department_products in departments_with_products:
        departments_with_products[department_products] = dict(heapq.nlargest(
            5, departments_with_products[department_products].items(), key=itemgetter(1)))

    return departments_with_products


def indicadores(request):  # retornahttpresponse
    return HttpResponse("Hey1")


def tablas(request):  # retornahttpresponse
    return HttpResponse("Hey1")


def visualizador(request):  # retornahttpresponse
    return HttpResponse("Hey1")
