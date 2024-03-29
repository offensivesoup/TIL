from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    # url -> view -> template(없을 수도 있지만)
    path('', views.index, name = 'index'),
    path('create/',views.create, name = 'create'),
]
