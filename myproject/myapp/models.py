from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField()
    
    def __str__(self):
        return self.category_name
    


# =============== one to many =============================
# ================ mode.CASCADE

class Product(models.Model):
    product_category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True) # setnull #cascade
    p_name = models.CharField()
    p_color = models.CharField()
    p_size = models.CharField()
    p_qty = models.PositiveIntegerField()
    p_photo = models.ImageField(upload_to='product')
    p_prize = models.PositiveIntegerField()
    p_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.p_name
    
# ================== one to one ===========================
# on_delete=models.CASCATD



class Cart(models.Model):
    cart_itme = models.ForeignKey(Category, on_delete=models.CASCADE)
    cart_name = models.CharField()
    cart_color = models.CharField()
    cart_size = models.CharField()
    cart_prize = models.PositiveIntegerField()
    cart_qty = models.PositiveIntegerField()
    
    cart_photo = models.ImageField(upload_to='cart')
    car_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_name
    
    

    
 
    
    
