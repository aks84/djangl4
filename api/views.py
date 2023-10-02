from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, RestaurantsSerializer, EmployeesSerializer, CustomersSerializer, MenuItemsSerializer, OrdersSerializer, OrderDetailsSerializer, InventorySerializer, ThirdPartyPlatformsSerializer, ThirdPartyOrdersSerializer, TableReservationsSerializer, PaymentsSerializer, ReviewsSerializer


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


class Restaurants(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
    permission_classes = [permissions.IsAuthenticated]


class Employees(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [permissions.IsAuthenticated]


class Customers(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuItems(viewsets.ModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer
    permission_classes = [permissions.IsAuthenticated]


class Orders(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDetails(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]


class Inventory(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ThirdPartyPlatforms(viewsets.ModelViewSet):
    queryset = ThirdPartyPlatforms.objects.all()
    serializer_class = ThirdPartyPlatformsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ThirdPartyOrders(viewsets.ModelViewSet):
    queryset = ThirdPartyOrders.objects.all()
    serializer_class = ThirdPartyOrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class TableReservations(viewsets.ModelViewSet):
    queryset = TableReservations.objects.all()
    serializer_class = TableReservationsSerializer
    permission_classes = [permissions.IsAuthenticated]


class Payments(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]


class Reviews(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticated]

