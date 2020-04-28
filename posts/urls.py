from django.urls import path
from . import views
from .views import CreatePostView

urlpatterns = [
    path('create/',CreatePostView.as_view(), name="create_post"),
]
