from django.shortcuts import render,redirect
from myapp.models import Product,Category,Cart

# Create your views here.

def indexView(request):
    
    cat = Category.objects.all()
    
    
    
    
    p_data = Product.objects.all()
    
    
    context = {'p_data':p_data, 'cat':cat}
    return render(request,'index.html',context)


# def indexView(request,str):
    
#     cat = Category.objects.all()
    
#     p_data = Product.objects.all
#     p_home = Product.objects.filter(str='Home')
#     p_car = Product.objects.filter(str='Car')
#     p_flower = Product.objects.filter(str='Flower')
    
    
#     context = {'p_all':p_data,'p_home':p_home, 'p_car':p_car,'p_flower':p_flower, 'cat':cat}
#     return render(request,'index.html',context)

def baseView(request):
    return render(request,'base.html')

def cartView(request,id):
    c_data = Cart.objects.all
    context = {'c_data':c_data}
    
    
    
    
    p_data = Product.objects.get(id=id)
    
    
    Cart.objects.create( 
                        cart_itme = p_data.product_category,
                        cart_name = p_data.p_name,
                        cart_color = p_data.p_color,
                        cart_size = p_data.p_size,
                        cart_prize = p_data.p_prize,
                        cart_qty = p_data.p_qty,
                        cart_photo = p_data.p_photo )
    
    
    
    return render(request, 'cart.html', context)
