from .models import Order
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def acceptance_of_order(request):
    id_order = int(request.POST.get('id_order', ''))
    order = Order.objects.get(pk = id_order)
    order.status = 'accepted'
    order.save()

    return HttpResponse('OK')