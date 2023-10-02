from django.contrib.auth.models import User, Group, Restaurants, Employees, Customers, MenuItems, Orders, OrderDetails, Inventory, ThirdPartyPlatforms, ThirdPartyOrders, TableReservations, Payments, Reviews
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        

class RestaurantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class MenuItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class ThirdPartyPlatformsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThirdPartyPlatforms
        fields = '__all__'


class ThirdPartyOrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThirdPartyOrders
        fields = '__all__'


class TableReservationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TableReservations
        fields = '__all__'


class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

