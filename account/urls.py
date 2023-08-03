from django.urls import path
from .views import *


urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    path('forgot_password/',forgot_password,name='forgot_password'),
    path('verify_otp<int:id>/',verify_otp,name='verify_otp'),
    path('password_change<int:id>',password_change,name='password_change')
]