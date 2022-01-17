from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from common.models import Customer
def listcustomers(request):
    qs = Customer.objects.values()
    return HttpResponse(qs)
