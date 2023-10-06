from django.db import models
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
    seller = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    auction = models.ForeignKey('Auction', on_delete=models.CASCADE)
    bidder = models.ForeignKey('User', on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField()

    def __str__(self):
        return f"Bid {self.bid_id} - Auction {self.auction.auction_id}"


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=50)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)
#     full_name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.username

