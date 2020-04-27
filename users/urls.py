from .views import *
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/logout/', LogoutView.as_view(), name="auth-logout"),
    path('register/verify/code=<str:token>/',SetPasswordAndActivate,name="email-activator"),
    path('register/',RegistrationView.as_view(),name="registration"),
    path('resetpassemail/',ResetPasswordEmail,name="resetpass_email"),
    path('resetpass/code=<str:token>/',ResetPassword,name="resetpass"),
    path('follow/', FollowUserView.as_view(), name="follow-user"),
]
