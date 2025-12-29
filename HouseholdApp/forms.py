from django import forms
from MyApp.models import tbl_PickupRequest, tbl_HouseholdPayment, tbl_BinType
import datetime

class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = tbl_PickupRequest
        fields = ['scheduled_date', 'request_time', 'bin_type']
        widgets = {
            'scheduled_date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control',
                'required': True,
                'min': datetime.date.today().isoformat(),
                'title': 'Please select a future date'
            }),
            'request_time': forms.TimeInput(attrs={
                'type': 'time', 
                'class': 'form-control',
                'required': True,
                'title': 'Please select a time'
            }),
            'bin_type': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
                'title': 'Please select a bin type'
            }),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = tbl_HouseholdPayment
        fields = ['bin_type', 'payment_for_date']
        widgets = {
            'payment_for_date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control',
                'required': True,
                'max': datetime.date.today().isoformat(),
                'title': 'Please select a valid date'
            }),
            'bin_type': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
                'title': 'Please select a bin type'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bin_type'].label = "Select Bin Type"
        self.fields['payment_for_date'].label = "Payment For Date"
