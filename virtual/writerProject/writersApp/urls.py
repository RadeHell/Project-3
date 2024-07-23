from django.urls import path
from .views import *

urlpatterns = [
    path('', views.Main , name='Main'),
    path('Writers/', views.Writers , name='Writers'),
    path('Books/', views.Books , name='Books'),
    path('Orders/', views.Orders , name='Orders'),
    path('Home/', views.Home , name='Home'),
    path('AboutPage/', views.About , name='About'),
    path('list/',BookListView.as_view(),name='book_list'),
    path('create/',BookCreateView.as_view(),name='')

]