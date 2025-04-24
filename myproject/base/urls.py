
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('addtocart/<int:pk>',views.addtocart,name='addtocart'),
    path('removecartitem/<int:pk>',views.removecartitem,name='removecartitem'),
    path('support',views.support,name='support'),
]