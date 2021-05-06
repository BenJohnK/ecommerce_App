from django.contrib.auth.models import User
from .models import Customer
from django.db.models.signals import post_save

def create_customer(sender,instance,created,**kwargs):
    if created:
        if not instance.is_superuser:
            Customer.objects.create(user=instance,name=instance,email=instance.email)
post_save.connect(create_customer,sender=User)

def update_customer(sender,instance,created,**kwargs):
    if created==False:
        if not instance.is_superuser:
            instance.customer.save()
post_save.connect(update_customer,sender=User)

