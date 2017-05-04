from django import forms
from .models import Product, Review


class ProductAddForm(forms.ModelForm):

    class Meta:

        model = Product
        fields = {
            'title',
            'description',
            'price',
        }
