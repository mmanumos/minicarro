from django.contrib import admin
from .models.product import Product
from .models.order import Order, OrderItems


# Models recorded.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItems)
