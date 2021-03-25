from django.urls import path,include
from . views import store,loginPage,registerPage,logoutPage,updateCart,cartPage

urlpatterns = [
    path('',store,name="store"),
    path('login/',loginPage,name="login"),
    path('register/',registerPage,name="register"),
    path('logout/',logoutPage,name="logout"),
    path('update_cart/',updateCart,name="update_cart"),
    path('cart/',cartPage,name="cart")
]

