from django.urls import path
from .views import CreateSession, ItemView, ItemsView, cancel, SuccessView, CreateOrder

urlpatterns = [
    path('buy/<int:id>/', CreateSession.as_view(type='item'), name='create_session'),
    path('buy/order/<int:id>/', CreateSession.as_view(type='order'), name='create_session_order'),
    path('item/<int:item_id>/', ItemView.as_view(), name='item_view'),
    path('cancel/', cancel),
    path('success/', SuccessView.as_view(), name='success'),
    path('createorder/', CreateOrder.as_view(), name='create_order'),
    path('', ItemsView.as_view(), name='items_list')
]