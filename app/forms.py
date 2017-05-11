from django import forms
from django.contrib.auth.models import User

from .models import Category, Product


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'price', 'created_at', 'modified_at']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']