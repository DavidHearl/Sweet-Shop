from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name='view_shopping_bag'),
    path('add/<item_id>/', views.add_to_shopping_bag, name='add_to_shopping_bag'),
]