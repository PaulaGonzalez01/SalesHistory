from django.db import models

# Create your models here.


class Department(models.Model):
    department_id = models.CharField(max_length=6, primary_key=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class Product(models.Model):
    product_id = models.CharField(max_length=6, primary_key=True)
    product_name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    margin = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.CharField(max_length=6, primary_key=True)
    order_hour_of_day = models.DateField()

    def __str__(self):
        return self.order_id


class OrderProduct(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
