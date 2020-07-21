from django.shortcuts import render,redirect
from django.http import HttpResponse
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from ..models.orders import Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class CheckOut(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        print(address , phone , customer ,cart , products)
        for product in products:
            order=Order(customer=Customer(id=customer),product=product,price=product.price,quantity=cart.get(str(product.id)),address=address,phone=phone)
            order.placeOrder()
            
        request.session['cart']={}
        return redirect('cart')

