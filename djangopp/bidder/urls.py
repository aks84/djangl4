from django.urls import include, path
from rest_framework import routers
from .views import *

bidurl = routers.DefaultRouter()
bidurl.register(r'users', UserViewSet)
bidurl.register(r'groups', GroupViewSet)

bidurl.register(r'bids', BidViewSet)
bidurl.register(r'auctions', AuctionViewSet)
bidurl.register(r'items', ItemViewSet)
bidurl.register(r'bidders', BidderViewSet)
