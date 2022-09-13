from django.urls import reverse
from django.views.generic.base import View, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect, get_object_or_404, render, get_list_or_404, HttpResponse
from django.http import JsonResponse
from config.settings import STRIPE_PK
from .models import Item, Order
from .stripe_defs import create_session


class CreateSession(View):
    type = ''
    def get(self, request, **kwargs):
        if self.type == 'item':
            item = get_object_or_404(Item, pk=kwargs['id'])
            return JsonResponse(create_session(item.currency, item.name, item.price))
        if self.type == 'order':
            order = get_list_or_404(Order, number=kwargs['id'])
            price = 0
            for item_ in order:
                price += item_.item.price
            return JsonResponse(create_session(item_.item.currency, 'Заказ'+str(kwargs['id']), price))


class ItemView(DetailView):
    template_name = 'item.html'
    model = Item
    pk_url_kwarg = 'item_id'
    extra_context = {'STRIPE_PK': STRIPE_PK}


class ItemsView(ListView):
    model = Item
    template_name = 'items.html'


class SuccessView(TemplateView):
    template_name = 'success.html'


class CreateOrder(View):
    def post(self, request):
        items = []
        price = 0
        if Order.objects.first():
            num = Order.objects.order_by('number').last().number + 1
        else:
            num = 1
        for item in Item.objects.all():
            if request.POST.get(str(item.pk)):
                if items:
                    if items[-1].currency != item.currency:
                        return render(request, 'order_error_1.html')
                order = Order.objects.create(number=num, item=item)
                items += [item]
                price += item.price
        if not items:
            return render(request, 'order_error_2.html')
        return render(request, 'order.html', {'items': items, 'price': price,
                                              'order': order, 'STRIPE_PK': STRIPE_PK})


def cancel(request):
    return redirect('/')
