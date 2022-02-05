from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
# Create your views here.

from product.models import Product
from member.models import Mem
from django.db.models import Q
from .forms import OrderAddForm
from cart.models import Cart
from order.models import Order, OrderItem
from datetime import datetime
from member.members import mem_check

def order_add(request):
    
    member = get_object_or_404(Mem, Mem_id=request.session['member_id'])
    cart_list = member.cart_set.all()
    

        
    
    if request.method == 'POST':
        ## 주문서 아이디 생성
        today = datetime.now()
        order_id = today.strftime('%Y%m%d%H%M%S')
        ## 별도 주문서 아이디
        print(order_id)
        
        form = OrderAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for item in cart_list:
            ##상품정보 재고수량과 장바구니의 주문수량비교
                if item.product.pro_stock >= item.amount:
                    item.product.pro_stock = item.product.pro_stock-item.amount
                    item.product.save()
                else:
                    #member = get_object_or_404(Mem, Mem_id=request.session['member_id'])
                    return HttpResponseRedirect(reverse('cart:detail'))
                 
            ## 주문서 정보에 데이터 입력
            order = Order(order_id=order_id, member_id=member.id, \
                       order_name=cd['order_name'], order_tel=cd['order_tel'], order_addr=cd['order_addr'], order_status='주문완료')
            order.save()
            print(order.id)
            # 주문서 테이블의 기본키
            ## 장바구니 그대로 주문 아이템에 등록
            for item in cart_list:
                OrderItem(order_id=order.id, product_id=item.product_id, price=item.price, \
                          amount=item.amount).save()
                ## 상품 테이블에 있는 재고수량을 감소

            ## 주문 아이템에 등록하고 장바구니 삭제
            Cart.objects.filter(member_id=member.id).delete()
            
            return render(request, 'order/add_ok.html', {'order':order, 'member':member})
    else:        
        cart_total = 0
        for item in cart_list:        
            cart_total += item.total
        form = OrderAddForm(initial={'order_name':member.Mem_name, \
                                     'order_tel':member.Mem_tel, 'order_addr':member.Mem_addr})

        return render(request, 'order/add.html', {'cart_list':cart_list, 'member':member, 'form':form, 'cart_total':cart_total})

def order_ok(request):
    pass

def order_list(request):
    member = get_object_or_404(Mem, Mem_id=request.session['member_id'])
    order_list = member.order_set.all()
    return render(request, 'order/list.html',{'order_list':order_list, 'member':member})
    #member = mem_check(request)
    #error_message = ''
     #   if member==None:
      #      return HttpResponseRedirect(reverse('member:login'))
       # else:
        #    order_list = member.order_set.all()
            #return render(request, 'order/list.html',{'order_list':order_list, 'member':member})
    
def order_detail(request, pk):
    member= get_object_or_404(Mem, Mem_id=request.session['member_id'])
    order = get_object_or_404(Order, id=pk)
    return render(request, 'order/detail.html', {'order':order, 'member':member})
    