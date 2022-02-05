from django.urls import path
from order.views import *
from order import views

app_name = 'order'

urlpatterns = [
    path('add', order_add, name='order_add'),
    path('list', order_list, name='order_list'),
    path('detail/<int:pk>', order_detail, name='order_detail'),
    #path('remove/<int:cart_id>/', remove, name='cart_remove'),
    #path('mod/<int:cart_id>/', mod, name='cart_mod'),
]