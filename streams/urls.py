from django.urls import path
from .views import *

urlpatterns = [
    path('follow/', FollowStreamView.as_view(), name="follow_stream"),
]
