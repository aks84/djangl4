from django.urls import include, path
from djangopp.api.urls import apiurl
from djangopp.bidder.urls import bidurl


urlpatterns = [
    path('api/', include(apiurl.urls)),
    path('bid/', include(bidurl.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]