from django.http import HttpResponse
from .models import Order

def expectation_of_taxist(request):
    id_order = int(request.GET.get('id_order', ''))

    while Order.objects.get(pk = id_order).status == 'expectation':
        pass

    if Order.objects.get(pk = id_order).status == 'canceled':
        pass
    else:
        pass
    
    return HttpResponse('OK')