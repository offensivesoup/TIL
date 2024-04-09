from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
    # variable routing 사용 중
    path('<str:username>/profile', views.profile, name = 'profile'),
    path('<int:profile_owner_pk>/follow', views.follow, name = "follow"),
]
