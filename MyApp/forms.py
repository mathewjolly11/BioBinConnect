from django import forms

from MyApp.models import  tbl_District, tbl_location, tbl_residentsassociation, tbl_Route, tbl_CollectorAssignment, tbl_BinType

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
    assign_all_week = forms.BooleanField(
        required=False,
        initial=False,
        label='Assign for All Week',
        help_text='Check this to assign the collector to this route for all days of the week',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'assign_all_week'
        })
    )
    
    class Meta:
        model = tbl_CollectorAssignment
        fields = ['Assign_id', 'collector', 'Route_id', 'day_of_week']
        labels = {
            'collector': 'Collector:',
            'Route_id': 'Route id:',
            'day_of_week': 'Day of week:',
        }
        widgets = {
            'Assign_id': forms.HiddenInput(),
            'day_of_week': forms.Select(choices=[
                ('', 'Select Day'),
                ('Monday', 'Monday'),
                ('Tuesday', 'Tuesday'),
                ('Wednesday', 'Wednesday'),
                ('Thursday', 'Thursday'),
                ('Friday', 'Friday'),
                ('Saturday', 'Saturday'),
                ('Sunday', 'Sunday'),
            ], attrs={
                'class': 'form-control',
                'id': 'day_of_week_select',
                'style': 'width: 100%;'
            }),
            'collector': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
                'style': 'width: 100%;'
            }),
            'Route_id': forms.Select(attrs={
                'class': 'form-control',
                'required': True,
                'style': 'width: 100%;'
            })
        }
    
    def __init__(self, *args, **kwargs):
        from GuestApp.models import Collector
        from MyApp.models import tbl_Route
        
        super().__init__(*args, **kwargs)
        
        # Set up collector choices
        self.fields['collector'].queryset = Collector.objects.filter(is_active=True).order_by('collector_name')
        self.fields['collector'].empty_label = 'Select Collector'
        
        # Set up route choices
        self.fields['Route_id'].queryset = tbl_Route.objects.all().order_by('name')
        self.fields['Route_id'].empty_label = 'Select Route'
        
        # Make day_of_week not required by default since it can be overridden by assign_all_week
        self.fields['day_of_week'].required = False
        
        # Add help text for better user experience
        self.fields['collector'].help_text = 'Choose an approved collector from the list'
        self.fields['Route_id'].help_text = 'Select the route for waste collection'
        self.fields['day_of_week'].help_text = 'Choose a specific day or select "Assign for All Week" below'

class BinTypeForm(forms.ModelForm):
    class Meta:
        model = tbl_BinType
        fields = ['BinType_id', 'name', 'capacity_kg', 'price_rs']
        widgets = {
            'BinType_id': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bin Type Name (e.g., Medium, Large)',
                'required': True,
                'minlength': '2',
                'maxlength': '50',
                'pattern': '[a-zA-Z\\s]+',
                'title': 'Bin type name should only contain letters and spaces'
            }),
            'capacity_kg': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Capacity in kg',
                'required': True,
                'min': '1',
                'max': '1000',
                'step': '1',
                'title': 'Please enter a valid capacity in kilograms'
            }),
            'price_rs': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price in Rupees',
                'required': True,
                'min': '0.01',
                'max': '10000',
                'step': '0.01',
                'title': 'Please enter a valid price'
            })
        }
