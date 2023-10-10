from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from djangopp.api.serializers import *
from djangopp.api.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ThirdPartyPlatformViewSet(viewsets.ModelViewSet):
    queryset = ThirdPartyPlatforms.objects.all()
    serializer_class = ThirdPartyPlatformsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ThirdPartyOrderViewSet(viewsets.ModelViewSet):
    queryset = ThirdPartyOrders.objects.all()
    serializer_class = ThirdPartyOrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class TableReservationViewSet(viewsets.ModelViewSet):
    queryset = TableReservations.objects.all()
    serializer_class = TableReservationsSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticated]

