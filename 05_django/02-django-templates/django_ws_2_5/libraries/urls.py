from django.contrib import admin
from django.urls import path
from libraries import views

urlpatterns = [
    path('recommend/', views.recommend),
    path('bestseller/', views.bestseller),
    ]