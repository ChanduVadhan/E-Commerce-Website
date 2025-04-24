from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    p_category=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    p_desc=models.CharField(max_length=100)
    p_price=models.IntegerField(default=0)
    p_images=models.ImageField(default='default.png',upload_to='uploads')
    p_trending=models.BooleanField(default=0)
    p_offer=models.BooleanField(default=0)

    def __str__(self):
        return self.p_name
    

class CartModel(models.Model):
    p_category=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    p_desc=models.CharField(max_length=100)
    p_price=models.IntegerField(default=0)
    p_quatity=models.IntegerField(default=1)
    totalamount=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.p_name