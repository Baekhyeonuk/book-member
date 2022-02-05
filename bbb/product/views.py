
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from product.models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from member.models import Mem

from django.conf import settings
import os
from cart.forms import AddProForm
from product.forms import ProSearchForm
try:
    from django.utils import simplejson as json
except ImportError:
    import json


class ProdListView(ListView):
    model = Product
    #queryset = Product.objects.filter(pro_display=1)
    ## 모델명(소문자)_list.html
    paginate_by = 3
    template_name = 'product/list.html'
    ## object_list 로 객체 반환
    
# class ProdDetailView(DetailView):
#     model = Product
#     ## 모델명(소문자)_detail.html
#     template_name = 'product/detail.html'
#     ## object 로 객체 반환
    
def detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    add_to_cart = AddProForm()
    return render(request, 'product/detail.html', {'product':product, 'add_to_cart':add_to_cart})

def search(request):

    form = ProSearchForm(request.POST)
    if form.is_valid():
            cd = form.cleaned_data
            search_item = cd['search_word']
            
    product_list = Product.objects.filter(Q(pro_name__contains=search_item) & Q(pro_display=1))
    return render(request, 'product/search.html', {'product_list':product_list, 'search_item':search_item})

class ProdAddView(CreateView):
    model = Product
    fields = ['Mem_id','Mem_name', 'Mem_pwd']
    success_url = reverse_lazy('product:list')
    template_name = 'product/add.html'
    
def like(request):
    if request.method == 'POST':
        product_id = request.POST['pk']
        product = Product.objects.get(pk = product_id)
        product.pro_like +=1
        product.save()
        message = 'You liked this'
    context = {'likes_count' : product.pro_like, 'message' : message}

    return HttpResponse(json.dumps(context), content_type='application/json')


# def add(request):
#     form=Mem()    
#     if request.method == "POST":
#         
#         if request.FILES:
#             form.Mem_img = request.FILES['upload_files']
#         else:
#            form.Mem_img = ''
# 
#         form.Mem_id=request.POST['mem_id']
#         form.Mem_name=request.POST['mem_name']
#         form.Mem_pwd=request.POST['mem_pwd']
#         form.save()
#         return HttpResponseRedirect(reverse('member:list'))
# 
#     else:
#         return render(request, 'member/add2.html')