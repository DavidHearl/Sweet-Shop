from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_completed_successfully/<order_number>', views.checkout_completed_successfully, name='checkout_completed_successfully'),
]