from django.db import models
from django.contrib.auth.models import User
from sqlalchemy.orm import relationship
from .product import Product


class Order(models.Model):
    """ Class to define attributes, getters and data for Orders """
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, related_name="user_order", on_delete=models.CASCADE)
    status = models.IntegerField()
    list_items = relationship("OrderItems", backref="Order")

    def __str__(self):
        return "Order " + str(self.id)

    @property
    def list_items(self):
        """ Getter method to return all items asociated to an order """
        order_items = OrderItems.objects.filter(order_id=self)
        list_elements = []
        for obj in order_items:
            list_elements.append([obj.product_id, obj.cant])
        print(list_elements)
        return list_elements


class OrderItems(models.Model):
    """ Class to define associated products to an order """
    order_id = models.ForeignKey(
        Order, related_name="orderItem_order", on_delete=models.CASCADE)
    product_id = models.ForeignKey(
        Product, related_name="order_product", on_delete=models.CASCADE)
    cant = models.IntegerField()

    def __str__(self):
        return "Order " + str(self.order_id.id) + " -  " + str(self.product_id.name)
