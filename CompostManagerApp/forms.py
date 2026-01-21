from django import forms
from MyApp.models import tbl_CompostBatch

class CreateCompostBatchForm(forms.ModelForm):
    """Form for creating new compost batches (only batch name required)"""
    
    class Meta:
        model = tbl_CompostBatch
        fields = ['Batch_name']
        widgets = {
            'Batch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter batch name'}),
        }
        labels = {
            'Batch_name': 'Batch Name',
        }


class CompostBatchForm(forms.ModelForm):
    """Form for creating and editing compost batches"""
    
    class Meta:
        model = tbl_CompostBatch
        fields = ['Batch_name', 'Grade', 'price_per_kg', 'Source_Waste_kg', 'Stock_kg']
        widgets = {
            'Batch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter batch name'}),
            'Grade': forms.Select(attrs={'class': 'form-control'}),
            'price_per_kg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price per kg', 'step': '0.01'}),
            'Source_Waste_kg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter source waste in kg', 'step': '0.01'}),
            'Stock_kg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter current stock in kg', 'step': '0.01'}),
        }
        labels = {
            'Batch_name': 'Batch Name',
            'Grade': 'Compost Grade',
            'price_per_kg': 'Price per KG (₹)',
            'Source_Waste_kg': 'Source Waste (kg)',
            'Stock_kg': 'Current Stock (kg)',
        }
    
    def clean_Source_Waste_kg(self):
        value = self.cleaned_data.get('Source_Waste_kg')
        if value and value <= 0:
            raise forms.ValidationError('Source waste must be greater than 0')
        return value
    
    def clean_price_per_kg(self):
        value = self.cleaned_data.get('price_per_kg')
        if value and value <= 0:
            raise forms.ValidationError('Price must be greater than 0')
        return value
    
    def clean_Stock_kg(self):
        value = self.cleaned_data.get('Stock_kg')
        if value and value < 0:
            raise forms.ValidationError('Stock cannot be negative')
        return value


class BatchStatusUpdateForm(forms.Form):
    """Form for updating batch status"""
    
    STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Ready', 'Ready for Sale'),
    ]
    
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
