from django.urls import path
from .views import *

urlpatterns = [
    path('follow/', FollowStreamAPI, name="follow_stream"),
]

