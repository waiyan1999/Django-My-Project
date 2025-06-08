from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',indexView, name = 'index'),
    path('base/',baseView, name = 'base'),
    path('cart/<int:id>', cartView , name = 'cart')
]