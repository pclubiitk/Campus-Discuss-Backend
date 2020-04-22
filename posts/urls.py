from django.urls import path
from . import views
from .views import CreatePost

urlpatterns = [
    path('create/',CreatePost, name="create_post"),
]
