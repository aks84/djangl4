from django.urls import include, path
from rest_framework import routers
from .views import *

apiurl = routers.DefaultRouter()
apiurl.register(r'users', UserViewSet)
apiurl.register(r'groups', GroupViewSet)

apiurl.register(r'restaurants', RestaurantViewSet)
apiurl.register(r'employees', EmployeeViewSet)
apiurl.register(r'customers', CustomerViewSet)
apiurl.register(r'menu-items', MenuItemViewSet)
apiurl.register(r'orders', OrderViewSet)
apiurl.register(r'order-details', OrderDetailViewSet)
apiurl.register(r'inventories', InventoryViewSet)
apiurl.register(r'tpp', ThirdPartyPlatformViewSet)
apiurl.register(r'tpo', ThirdPartyOrderViewSet)
apiurl.register(r'tr', TableReservationViewSet)
apiurl.register(r'payments', PaymentViewSet)
apiurl.register(r'reviews', ReviewViewSet)