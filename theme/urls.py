from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainpageView.as_view(), name='main'),
    path('map/', Map.as_view(), name='map'),
    # path('video/', Video.as_view(), name='video'),
    # path('video_detail/', VideoDetail.as_view(), name='video_detail'),
]