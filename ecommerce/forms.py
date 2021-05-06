from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CreateProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={'placeholder':'Enter Product Name','class':'form-control','style':'width:100%'}),
            "price":forms.NumberInput(attrs={'placeholder':'Enter Product Price','class':'form-control','style':'width:100%'}),
            "description":forms.TextInput(attrs={'placeholder':'Enter Product Description','class':'form-control','style':'width:100%'}),
        }
