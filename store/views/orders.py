from django.shortcuts import render,redirect
from django.http import HttpResponse
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from ..models.orders import Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from ..middlewares.auth import auth_middleware

class OrderView(View):
      
      def get(self,request):
        customer=request.session.get('customer')
        orders=Order.get_orders_by_customer(customer)
        orders=orders.reverse()
      #   print(orders)
        return render(request,'orders.html',{'orders':orders})
