from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('register/', views.register_user, name="register"),
    # path('login/', views.login_user, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/admin/', views.adminLogin, name="admin_login"),
]
