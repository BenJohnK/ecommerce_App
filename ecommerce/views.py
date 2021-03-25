from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from . decorators import is_authenticated
from . models import *
import json

# Create your views here.


@login_required(login_url='/login/')
def store(request):
    products=Product.objects.all()
    customer=request.user.customer
    order,created=Order.objects.get_or_create(customer=customer,completed=False)
    cart_items_total=order.cart_items_count
    return render(request,"ecommerce/index.html",{'products':products,'cart_items_total':cart_items_total})

@is_authenticated
def registerPage(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, "Account Created for "+username)
            return redirect('/login/')
    return render(request,"ecommerce/register.html",{'form':form})

@is_authenticated
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Incorrect Username or Password!")
    return render(request,"ecommerce/login.html",{})

def logoutPage(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def updateCart(request):
    data=json.loads(request.body)
    productid=data['productid']
    action=data['action']
    product=Product.objects.get(id=productid)
    customer=request.user.customer
    order=Order.objects.get(customer=customer,completed=False)
    orderitem,created=OrderItem.objects.get_or_create(order=order,product=product)
    if action == "add":
        orderitem.quantity+=1
        orderitem.save()
    else:
        if orderitem.quantity>1:
            orderitem.quantity-=1
            orderitem.save()
        else:
            orderitem.delete()   #to be reviewed for decrease button
    

    return JsonResponse('reached backend',safe=False)

@login_required(login_url='/login/')
def cartPage(request):
    customer=request.user.customer
    order=Order.objects.get(customer=customer,completed=False)
    order_items=order.orderitem_set.all()
    cart_items_total=order.cart_items_count

    return render(request,"ecommerce/cart.html",{'order':order,'order_items':order_items,'cart_items_total':cart_items_total})