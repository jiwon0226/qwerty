
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path( '', views.home, name= "home"),
    path('move.', views.move, name="move"),
    path('add/', views.add, name="add"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('signup/',views.sign_up, name="sign_up"),
]
