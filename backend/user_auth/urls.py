from django.urls import path
from user_auth import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name="user_register_view"),
    path('login/', views.UserLoginView.as_view(), name="user_login_view"),
]