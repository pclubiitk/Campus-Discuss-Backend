from django.urls import path
from .views import *

urlpatterns = [
    path('follow/', FollowStreamView.as_view(), name="follow_stream"),
    path('<int:pk>/posts/', PostsByStreamView.as_view(), name="posts_by _stream"),
    path('unfollow/' , UnfollowStreamView.as_view() , name="unfollow_stream"),
]
