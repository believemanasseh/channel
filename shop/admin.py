from django.contrib import admin

from shop.models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)


