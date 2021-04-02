from .models import Product
from django import forms


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
