from django.contrib import admin
from .models import Product, OrderProduct, Department, Order
# Register your models here.

admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Department)
