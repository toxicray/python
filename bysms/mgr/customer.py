import json

from django.http import JsonResponse
from common.models import Customer


def listCustomer(request):
    qs = Customer.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret': 0,'msg': retlist},
                        safe=False,
                        json_dumps_params={'ensure_ascii': False}
                        )


def addCustomer(request):
    pass


def modifyCustomer(request):
    pass


def deleteCustomer(request):
    pass

def dispatcher(request):

    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST','DELETE','PUT']:
        # json对象转化成字典对象
        request.params = json.loads(request.body)

    action = request.params['action']
    if action == 'list_customer':
        return listCustomer(request)
    elif action == 'add_customer':
        return addCustomer(request)
    elif action == 'modify_customer':
        return modifyCustomer(request)
    elif action == 'delete_customer':
        return deleteCustomer(request)
    else:
        return JsonResponse({'ret': 1,'msg': '不支持该类型的http请求'},
                            safe=False,
                            json_dumps_params={'ensure_ascii':False})