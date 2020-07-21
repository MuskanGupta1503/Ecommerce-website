from django.shortcuts import render,redirect
from django.http import HttpResponse
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        print(products)
        return render(request,'cart.html',{'products':products})