from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    d1=models.CharField(max_length=80,null=True)
    d2=models.CharField(max_length=80,null=True)
    d3=models.CharField(max_length=80,null=True)
    d4=models.CharField(max_length=80,null=True)
    d5=models.CharField(max_length=80,null=True,blank=True)
    d6=models.CharField(max_length=80,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(null=True)
    largeimage=models.ImageField(null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    completed=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def cart_items_count(self):
        order_item_list=self.orderitem_set.all()
        total=0
        for item in order_item_list:
            total+=item.quantity
        return total
    
    @property
    def order_total(self):
        order_item_list=self.orderitem_set.all()
        ordertotal=0
        for x in order_item_list:
            ordertotal+=(x.quantity*x.product.price)
        return ordertotal
        
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(null=True,default=0)

    def __str__(self):
        return str(self.id)
    
    @property
    def item_total(self):
        total=self.quantity*self.product.price
        return total

class ShippingDetails(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    country=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address

