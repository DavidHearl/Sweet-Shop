from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.all_products, name='products'),
     path('<int:product_id>/', views.product_detail, name='product_detail'),
     path('add/', views.add_product, name='add_product'),
     path('modify/<int:product_id>/',
          views.modify_product, name='modify_product'),
     path('modify_pricing/', views.modify_pricing, name='modify_pricing'),
     path('delete/<int:product_id>/',
          views.delete_product, name='delete_product'),
     path('delete_review/<int:review_id>/', views.delete_review,
          name='delete_review'),
     path('post_price/<int:product_id>/', views.post_price, name='post_price')
]
