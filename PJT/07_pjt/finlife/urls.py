from django.urls import path
from . import views
## REST API 제공

urlpatterns = [
    path('save-deposit-products/', views.save),
    path('deposit-products/', views.product_list),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.option_list),
    path('deposit-products/top-rate/', views.top_rated),
]