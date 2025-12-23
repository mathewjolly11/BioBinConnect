from django import forms

from MyApp.models import  tbl_District, tbl_location, tbl_residentsassociation, tbl_Route, tbl_CollectorAssignment

class DistrictForm(forms.ModelForm):
    class Meta:
        model = tbl_District
        fields = ['District_id', 'District_Name']
        widgets = {
            'District_id': forms.HiddenInput(),
        }

class LocationForm(forms.ModelForm):
   class Meta:
       model = tbl_location
       fields = ['Location_id', 'Ward_No', 'Ward_Name', 'District']
       widgets = {
           'Location_id': forms.HiddenInput(),
       }    

class RAForm(forms.ModelForm):
   class Meta:
       model = tbl_residentsassociation
       fields = ['RA_id', 'Location', 'Association_Name']
       widgets = {
           'RA_id': forms.HiddenInput(),
       }

class RouteForm(forms.ModelForm):
    class Meta:
        model = tbl_Route
        fields = ['Route_id', 'name', 'location', 'residents_association', 'start_house_no', 'end_house_no']
        widgets = {
            'Route_id': forms.HiddenInput(),
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
