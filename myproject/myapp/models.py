from django.db import models

# Create your models here.

class Product(models.Model):
    p_name = models.CharField()
    p_color = models.CharField()
    p_size = models.CharField()
    p_qty = models.PositiveIntegerField()
    p_photo = models.ImageField(upload_to='product')
    p_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.p_name
    
    
