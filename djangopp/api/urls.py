from django.urls import include, path
from rest_framework import routers
from djangopp.api.views import UserViewSet, GroupViewSet, RestaurantViewSet, EmployeeViewSet, CustomerViewSet, MenuItemViewSet, OrderViewSet, OrderDetailViewSet, InventoryViewSet, ThirdPartyPlatformViewSet, ThirdPartyOrderViewSet, TableReservationViewSet, PaymentViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

router.register(r'restaurants', RestaurantViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-details', OrderDetailViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'tpp', ThirdPartyPlatformViewSet)
router.register(r'tpo', ThirdPartyOrderViewSet)
router.register(r'tr', TableReservationViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'reviews', ReviewViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
