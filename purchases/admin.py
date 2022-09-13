from django.contrib import admin
from .models import Currency, Item, Order, Discount



class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'item')


admin.site.register(Currency)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount)
