from django.contrib import admin
from .models import Restaurants, Employees, Customers, MenuItems, Orders, OrderDetails, Inventory, ThirdPartyPlatforms, ThirdPartyOrders, TableReservations, Payments, Reviews

admin.site.register(Restaurants)
admin.site.register(Employees)
admin.site.register(Customers)
admin.site.register(MenuItems)
admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Inventory)
admin.site.register(ThirdPartyPlatforms)
admin.site.register(ThirdPartyOrders)
admin.site.register(TableReservations)
admin.site.register(Payments)
admin.site.register(Reviews)
