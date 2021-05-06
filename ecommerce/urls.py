from django.urls import path,include
from . views import store,loginPage,registerPage,logoutPage,updateCart,cartPage,checkoutPage,order_complete,admin_home,create,update

urlpatterns = [
    path('',store,name="store"),
    path('login/',loginPage,name="login"),
    path('register/',registerPage,name="register"),
    path('logout/',logoutPage,name="logout"),
    path('update_cart/',updateCart,name="update_cart"),
    path('cart/',cartPage,name="cart"),
    path('checkout/',checkoutPage,name="checkout"),
    path('order_complete/',order_complete,name="order_complete"),
    path('admin/home/',admin_home,name="admin_home"),
    path('admin/create/',create,name="create"),
    path('admin/update/<int:id>/',update,name="update")
]

