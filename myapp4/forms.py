from django import forms
from .models import Product



class ProductForm(forms.ModelForm):
    product = forms.ImageField()
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'photo']