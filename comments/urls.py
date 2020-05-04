from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateComment.as_view(), name="create-comment"),
    path('delete/', DeleteComment.as_view(), name="delete-comment"),
]

