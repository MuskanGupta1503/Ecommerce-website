from django.contrib import admin
from django.urls import path
from .views import home,signup,login
from .views.signup import Signup
from .views.login import Login,logout
from .views.home import Index
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from django.utils.decorators import method_decorator
from .middlewares.auth import auth_middleware

urlpatterns=[
    # path('',home.index,name='homepage'),
    path('',Index.as_view(),name='homepage'),
    path('signup/',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',CheckOut.as_view(),name='checkout'),
    path('orders',auth_middleware(OrderView.as_view()),name='orders'),
]