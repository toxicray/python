from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from common.models import Customer
def listcustomers(request):
    qs = Customer.objects.values()
    ph = request.GET.get('phonenumber', None)
    if ph:
        qs = qs.filter(ph)
    return HttpResponse(qs)
