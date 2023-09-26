from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)

class Menu(models.Model):
    contents = models.CharField(max_length=500)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant")
    day = models.CharField(max_length = 20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        f'Menu on {self.day}: {self.contents}'
    
class employee(models.Model):
    name = models.CharField(max_length=50,default="a")
    surname = models.CharField(max_length=50,default="b")
    username = models.CharField(max_length=50,default="ab")
    email = models.EmailField(default="example@email.com")
    password = models.CharField(max_length=30,default="password212")
    selectedMenu = models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True,default=None)