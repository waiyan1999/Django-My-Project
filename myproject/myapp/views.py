from django.shortcuts import render,redirect
from myapp.models import Product

# Create your views here.

def indexView(request):
    p_data = Product.objects.all()
    context = {'p_data':p_data}
    return render(request,'index.html',context)

def baseView(request):
    return render(request,'base.html')
