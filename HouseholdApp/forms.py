from django import forms
from MyApp.models import tbl_PickupRequest, tbl_HouseholdPayment, tbl_BinType

class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = tbl_PickupRequest
        fields = ['scheduled_date', 'request_time', 'bin_type']
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'request_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'bin_type': forms.Select(attrs={'class': 'form-control'}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = tbl_HouseholdPayment
        fields = ['bin_type', 'payment_for_date']
        widgets = {
            'payment_for_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'bin_type': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bin_type'].label = "Select Bin Type"
        self.fields['payment_for_date'].label = "Payment For Date"
