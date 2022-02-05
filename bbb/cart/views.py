from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
# Create your views here.

from product.models import Product
from member.models import Mem
from django.db.models import Q
from .forms import AddProForm
from cart.models import Cart

@require_POST
def add(request, product_id):

    if request.session.get('member_id') == None:
        messages.warning(request, "로그인 후 이용하세요")
        return HttpResponseRedirect(reverse('member:login'))

    else: 
        product = get_object_or_404(Product, id=product_id)
        ## 제품 정보
        member = get_object_or_404(Mem,Mem_id=request.session['member_id'])
        ## 사용자 정보
        # 유효성 검사, injection 전처리
        form = AddProForm(request.POST)
            
        if form.is_valid():
            cd = form.cleaned_data
            price = product.pro_price
            total = product.pro_price*cd['amount']
        else:
            pass
            
        try:
            cart = Cart.objects.get(Q(product_id=product_id) & Q(member_id=member.id))
        except (KeyError, Cart.DoesNotExist):
            ## 기존에 장바구니에 값이 없으면 장바구니에 새로 등록
            qry = Cart(product_id=product_id, member_id=member.id, \
                       amount=cd['amount'], total=total, price=price)
            qry.save()

        else:
            ## 기존에 등록 된 내용이 있으면  amout, total 갱신
            cart.amount += cd['amount']
            cart.total += total
            cart.price = price
            cart.save()
        return HttpResponseRedirect(reverse('cart:detail'))

def remove(request, cart_id):
    
    Cart.objects.filter(id=cart_id).delete()
    return HttpResponseRedirect(reverse('cart:detail'))
##    cart = Cart(request)
##    product = get_object_or_404(Product, id=product_id)
##    cart.remove(product)
##    return redirect('cart:detail')


def detail(request):
    
    member = get_object_or_404(Mem, Mem_id=request.session['member_id'])
    #cart_list = Cart.objects.filter(member_id=member.id)
    cart_list = member.cart_set.all()

   # add_to_cart = AddProForm()
    cart_total = 0
    for item in cart_list:
        cart_total += item.total
        item.add_to_cart = AddProForm(initial={'amount':item.amount})
        #print(item.product)

    return render(request, 'cart/detail.html', {'cart_list':cart_list , 'cart_total':cart_total , \
                                                'member':member})
                                                
@require_POST
def mod(request, cart_id):

    cart = get_object_or_404(Cart, id=cart_id)
    form = AddProForm(request.POST)
    
    if form.is_valid():
            cd = form.cleaned_data
            total = cart.price*cd['amount']
            cart.amount = cd['amount']
            cart.total = total
            cart.save()
            return HttpResponseRedirect(reverse('cart:detail'))
    else:
        return HttpResponseRedirect(reverse('cart:detail'))
        
def order(request):
    #print(request.POST['ct_id'])
    ct = request.POST.getlist('ct_id');
    print(ct)
    for i in ct:
        
        Cart.objects.filter(id=i).delete()

    return HttpResponseRedirect(reverse('cart:detail'))