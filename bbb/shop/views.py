from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from product.models import Product
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from product.forms import ProSearchForm

class HomeView(ListView):

    template_name = 'home.html'
    queryset = Product.objects.filter(pro_hot=1)


def home(request):

    ## 인기 상품
    h_list = Product.objects.filter(Q(pro_hot=1)  & Q(pro_display=1))
    ## 신규 상품
    n_list = Product.objects.filter(Q(pro_new=1)  & Q(pro_display=1))
    add_to_search = ProSearchForm()
    return render(request, 'home.html', {'h_list':h_list, 'n_list':n_list, 'add_to_search':add_to_search})
    

def hot(request):
    h_list = Product.objects.filter(Q(pro_hot=1)  & Q(pro_display=1))
    add_to_search = ProSearchForm()
    return render(request, 'hot.html', {'h_list':h_list, 'add_to_search':add_to_search})
    
def new(request):
    n_list = Product.objects.filter(Q(pro_new=1)  & Q(pro_display=1))
    add_to_search = ProSearchForm()
    return render(request, 'new.html', {'n_list':n_list, 'add_to_search':add_to_search})