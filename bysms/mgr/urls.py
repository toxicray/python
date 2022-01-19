from mgr import customer
from django.urls import path

urlpatterns = [
    path('customers', customer.dispatcher),
]