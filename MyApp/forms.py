from django import forms

from MyApp.models import  tbl_District, tbl_location, tbl_residentsassociation, tbl_Route, tbl_CollectorAssignment

class DistrictForm(forms.ModelForm):
    class Meta:
        model = tbl_District
        fields = ['District_id', 'District_Name']
        widgets = {
            'District_id': forms.HiddenInput(),
            'District_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'District Name',
                'required': True,
                'minlength': '2',
                'maxlength': '100',
                'pattern': '[a-zA-Z\s]+',
                'title': 'District name should only contain letters and spaces'
            })
        }

class LocationForm(forms.ModelForm):
   class Meta:
       model = tbl_location
       fields = ['Location_id', 'Ward_No', 'Ward_Name', 'District']
       widgets = {
           'Location_id': forms.HiddenInput(),
           'Ward_No': forms.NumberInput(attrs={
               'class': 'form-control',
               'placeholder': 'Ward Number',
               'required': True,
               'min': '1',
               'max': '999',
               'title': 'Please enter a valid ward number'
           }),
           'Ward_Name': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Ward Name',
               'required': True,
               'minlength': '2',
               'maxlength': '100',
               'pattern': '[a-zA-Z\s]+',
               'title': 'Ward name should only contain letters and spaces'
           }),
           'District': forms.Select(attrs={
               'class': 'form-control',
               'required': True,
               'title': 'Please select a district'
           })
       }    

class RAForm(forms.ModelForm):
   class Meta:
       model = tbl_residentsassociation
       fields = ['RA_id', 'Location', 'Association_Name']
       widgets = {
           'RA_id': forms.HiddenInput(),
           'Location': forms.Select(attrs={
               'class': 'form-control',
               'required': True,
               'title': 'Please select a location'
           }),
           'Association_Name': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Association Name',
               'required': True,
               'minlength': '3',
               'maxlength': '200',
               'title': 'Please enter a valid association name'
           })
       }

class RouteForm(forms.ModelForm):
    class Meta:
        model = tbl_Route
        fields = ['Route_id', 'name', 'location', 'residents_association', 'start_house_no', 'end_house_no']
        widgets = {
            'Route_id': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Route Name',
                'required': True,
                'minlength': '3',
                'maxlength': '100',
                'title': 'Please enter a valid route name'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
                'title': 'Please select a location'
            }),
            'residents_association': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
                'title': 'Please select a residents association'
            }),
            'start_house_no': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start House Number',
                'required': True,
                'min': '1',
                'max': '9999',
                'title': 'Please enter a valid starting house number'
            }),
            'end_house_no': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'End House Number',
                'required': True,
                'min': '1',
                'max': '9999',
                'title': 'Please enter a valid ending house number'
            })
        }

class CollectorAssignmentForm(forms.ModelForm):
    class Meta:
        model = tbl_CollectorAssignment
        fields = ['Assign_id', 'collector', 'Route_id', 'day_of_week']
        widgets = {
            'Assign_id': forms.HiddenInput(),
            'day_of_week': forms.Select(choices=[
                ('Monday', 'Monday'),
                ('Tuesday', 'Tuesday'),
                ('Wednesday', 'Wednesday'),
                ('Thursday', 'Thursday'),
                ('Friday', 'Friday'),
                ('Saturday', 'Saturday'),
                ('Sunday', 'Sunday'),
            ]),
        }
