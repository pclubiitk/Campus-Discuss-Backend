from .views import LoginView, LogoutView, ActivationMailer
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/logout/', LogoutView.as_view(), name="auth-logout"),
    path('verify/', ActivationMailer, name="activation-verify")
    # path('verify/', csrf_exempt(ActivationMailer))
]