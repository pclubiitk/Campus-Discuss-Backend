from .views import LoginView, LogoutView, ActivationMailer,SetPasswordAndActivate,ResetPasswordEmail,ResetPassword
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/logout/', LogoutView.as_view(), name="auth-logout"),
    path('verify/code=<str:token>/',SetPasswordAndActivate,name="email-activator"),
    path('verify/', ActivationMailer, name="activation-verify"),
    path('resetpassemail/',ResetPasswordEmail,name="resetpass_email"),
    path('resetpass/code=<str:token>/',ResetPassword,name="resetpass"),
    # path('verify/', csrf_exempt(ActivationMailer))
]



