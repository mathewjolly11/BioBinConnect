from django import forms
from MyApp.models import tbl_PickupRequest

class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = tbl_PickupRequest
        fields = ['scheduled_date', 'request_time']
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'request_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
