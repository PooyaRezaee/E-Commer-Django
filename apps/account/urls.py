from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path("register/", RegistretionUser.as_view(), name="register"),
    path("register/verify/", VerifyCode.as_view(), name="verify_code"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
