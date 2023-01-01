from django.forms import ModelForm
from django import forms
from .models import Category, Product



class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name-category-field field'}),
            'code': forms.TextInput(attrs={'class': 'code-category-field field'})
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'name-product-field  field',
                'placeholder': 'Product name'
            }),
            'quantity': forms.TextInput(attrs={'class': 'quantity-product-field  field'}),
            'category': forms.Select(attrs={'class': 'category-product-field  field'}),
            'format': forms.TextInput(attrs={'class': 'format-product-field  field'}),
            'code': forms.TextInput(attrs={
                'class': 'code-product-field  field',
                'placeholder': 'Product code'
            }),
            'notes': forms.TextInput(attrs={
                'class': 'notes-product-field  field',
                'placeholder': 'Product general notes'

            })
        }
