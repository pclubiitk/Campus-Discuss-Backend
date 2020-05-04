from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateAndDeleteBookmark.as_view(), name="create/delete-bookmark"),
]
