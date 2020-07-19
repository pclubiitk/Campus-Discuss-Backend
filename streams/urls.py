from django.urls import path
from .views import *

urlpatterns = [
    path('follow/', FollowStreamView.as_view(), name="follow-stream"),
    path('<int:pk>/posts/', PostsByStreamView.as_view(), name="posts_by _stream"),
    path('unfollow/', UnfollowStreamView.as_view(), name="unfollow-stream"),
    path('subbed/', SubbedStreamsView.as_view(), name="subbed-streams"),
    path('all/', AllStreamsView.as_view(), name="all-streams")
]
