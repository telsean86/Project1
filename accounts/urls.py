from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    path('register/', register, name='register'),
    path('delete/', delete, name='delete'),
    path('change_password/', change_password, name='change_password'),
    path('mypage/', mypage, name='mypage'),
    path('myboard/', myboard, name='myboard'),
]