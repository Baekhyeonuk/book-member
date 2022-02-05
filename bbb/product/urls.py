from django.urls import path
from product.views import *
from product import views

app_name = 'product'
urlpatterns = [
    path('', ProdListView.as_view(), name='list'),
    #path('detail/<int:pk>', ProdDetailView.as_view(), name='detail'),
    #path('detail/<int:product_id>', views.datail, name='detail'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('add/', ProdAddView.as_view(), name='add'),
    path('like', like, name='like'),
    
]