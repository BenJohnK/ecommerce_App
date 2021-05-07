from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import CreateUserForm,CreateProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from . decorators import is_authenticated,is_admin,admin_only
from . models import *
import json

# Create your views here.


@login_required(login_url='/login/')
@is_admin
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
    print("hit")
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
@is_admin
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
@is_admin
def cartPage(request):
    customer=request.user.customer
    order=Order.objects.get(customer=customer,completed=False)
    order_items=order.orderitem_set.all()
    cart_items_total=order.cart_items_count

    return render(request,"ecommerce/cart.html",{'order':order,'order_items':order_items,'cart_items_total':cart_items_total})

@login_required(login_url='/login/')
@is_admin
def checkoutPage(request):
    customer=request.user.customer
    order=Order.objects.get(customer=customer,completed=False)
    order_items=order.orderitem_set.all()
    cart_items_total=order.cart_items_count
    return render(request,"ecommerce/checkout.html",{'order':order,'order_items':order_items,'cart_items_total':cart_items_total})

@login_required(login_url='/login/')
@is_admin
def order_complete(request):
    data=json.loads(request.body)
    address=data['shippingdetails']['address']
    city=data['shippingdetails']['city']
    state=data['shippingdetails']['state']
    country=data['shippingdetails']['country']
    pincode=data['shippingdetails']['zipcode']
    customer=request.user.customer
    order=Order.objects.get(customer=customer,completed=False)
    order.completed=True
    order.save()
    ShippingDetails.objects.create(address=address,city=city,state=state,country=country,customer=customer,order=order)
    
    return JsonResponse('reached backend',safe=False)

@admin_only
def admin_home(request):
    print(request.get_full_path)
    products=Product.objects.all()
    return render(request,"ecommerce/admin_home.html",{'products':products})

@admin_only
def create(request):
    form=CreateProductForm()
    if request.method=='POST':
        form=CreateProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/home/')
    return render(request,"ecommerce/createform.html",{'form':form,'create':True})

@admin_only
def update(request,id):
    product=Product.objects.get(id=id)
    form=CreateProductForm(instance=product)
    if request.method=='POST':
        form=CreateProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/admin/home/')
    return render(request,"ecommerce/createform.html",{'form':form,'create':False})
    
@admin_only
def delete(request,id):
    product=Product.objects.get(id=id)
    if request.method=='POST':
        product.delete()
        return redirect('/admin/home/')
    return render(request,"ecommerce/deleteform.html",{'product':product})

def viewProduct(request,id):
    product=Product.objects.get(id=id)
    customer=request.user.customer
    order=Order.objects.get(customer=customer,completed=False)
    cart_items_total=order.cart_items_count
    return render(request,"ecommerce/viewproduct.html",{'product':product,'cart_items_total':cart_items_total})