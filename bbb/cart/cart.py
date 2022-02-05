from decimal import Decimal
from django.conf import settings

from product.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart_item')
        
        if not cart:
            cart = self.session['cart_item'] = {}
            
        self.cart = cart

    def add(self, product, amount):
        member_id = self.session.get('member_id')
        product_id = str(product.id)
        total = product.pro_price*amount
        if product_id not in self.cart:
            self.cart[product_id] = {'amount':amount, 'member_id':member_id, 'total':total}
        else:
            self.cart[product_id]['amount'] += amount
            self.cart[product_id]['total'] += total

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def save(self):
        self.session['cart_item'] = self.cart
        self.session.modified = True


