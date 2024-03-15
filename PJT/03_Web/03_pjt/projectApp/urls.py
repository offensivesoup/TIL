from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.project),
    path('project1/', views.project1)
]
