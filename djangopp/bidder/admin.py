from django.contrib import admin
from .models import Auction, Item, Bid, Bidder

admin.site.register(Auction)
admin.site.register(Item)
admin.site.register(Bid)
admin.site.register(Bidder)


