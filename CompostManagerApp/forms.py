from django import forms
from MyApp.models import tbl_CompostBatch

class CompostBatchForm(forms.ModelForm):
    """Form for creating and editing compost batches"""
    
    class Meta:
        model = tbl_CompostBatch
        fields = ['Batch_name']
        widgets = {
            'Batch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter batch name'}),
        }
        labels = {
            'Batch_name': 'Batch Name',
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
