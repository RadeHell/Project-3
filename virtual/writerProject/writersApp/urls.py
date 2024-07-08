from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main , name='Main'),
    path('Writers/', views.Writers , name='Writers'),
    path('Books/', views.Books , name='Books'),


]