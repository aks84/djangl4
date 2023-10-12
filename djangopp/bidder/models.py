from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Auction(models.Model):
    auction_id = models.AutoField(primary_key=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2)
    auction_status = models.CharField(max_length=20, choices=[('upcoming', 'Upcoming'), ('active', 'Active'), ('ended', 'Ended')])

    def __str__(self):
        return f"Auction {self.auction_id} - {self.item.item_name}"


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    seller = models.ForeignKey('Bidder', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    auction = models.ForeignKey('Auction', on_delete=models.CASCADE)
    bidder = models.ForeignKey('Bidder', on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField()

    def __str__(self):
        return f"Bid {self.bid_id} - Auction {self.auction.auction_id}"



class Bidder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    custom_groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    custom_user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username



