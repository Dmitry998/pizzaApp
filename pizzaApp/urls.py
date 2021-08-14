from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('order/<str:pk>/', views.order, name="customer"),
    path('pizza/<str:pk>/', views.pizza, name="pizza"),
]