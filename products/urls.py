from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('modify/<int:product_id>/',
         views.modify_product, name='modify_product'),
    path('delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
]
