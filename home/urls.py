from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.aboutUs, name="about_us"),
    path('fellowship/', views.schoolasiumFellowship, name="fellowship"),
]
