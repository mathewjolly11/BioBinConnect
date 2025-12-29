from django import forms
from MyApp.models import tbl_CollectionRequest

class CollectionLogForm(forms.ModelForm):
    class Meta:
        model = tbl_CollectionRequest
        fields = ['total_quantity_kg']
        widgets = {
            'total_quantity_kg': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter total weight in Kg',
                'step': '0.01',
                'min': '0.1',
                'max': '1000',
                'required': True,
                'title': 'Please enter weight between 0.1 and 1000 kg'
            })
        }
