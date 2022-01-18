from sales.views import listcustomers
from django.urls import path

urlpatterns = [
    path('customers', listcustomers),
]