from django.conf import settings
from django.contrib import messages
from django.template.context_processors import request

from coupon.models import Coupon
from shop.models import Product


class Cart(object):
    def __init__(self, request):  # 리스트로 저장?
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')

    def __len__(self):  # 몇개의 상품이 있는건지 보여주기 위함
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()  # 제품들 번호 목록을 가져옴

        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': product.price}

        if is_update:
            self.cart[product_id]['quantity'] = quantity
        elif product.stock < quantity:
            self.cart[product_id]['quantity'] = product.stock
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del (self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session['coupon_id'] = None
        self.session.modified = True

    def get_product_total(self, call='test'):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount_total(self):
        if self.coupon:
            if self.get_product_total() >= self.coupon.amount:
                return self.coupon.amount
        return int(0)

    def get_total_price(self):
        return self.get_product_total() - self.get_discount_total()
