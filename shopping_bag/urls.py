from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name='view_shopping_bag'),
    path('add/<item_id>/', views.add_to_shopping_bag, name='add_to_shopping_bag'),
    path('modify/<item_id>/', views.modify_shopping_bag, name='modify_shopping_bag'),
    path('remove/<item_id>/', views.remove_from_shopping_bag, name='remove_from_shopping_bag'),
]