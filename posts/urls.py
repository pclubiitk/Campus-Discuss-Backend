from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreatePostView.as_view(), name="create-post"),
    path('delete/', DeletePostView.as_view(), name="delete-post"),
]
