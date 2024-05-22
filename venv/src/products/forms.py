from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Product Title"
                }
        )
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Product Description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 10, 
                "cols": 30 
            }
        )
    )
    price = forms.DecimalField(
        initial=10.00,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Product Price"
            }
        )
    )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
        
        
    #validations    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "Product" not in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    
 
    

class RawProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Product Title"
                }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Product Description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 10, 
                "cols": 30 
            }
        )
    )
    price = forms.DecimalField(
        initial=10.00,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Product Price"
            }
        )
    )