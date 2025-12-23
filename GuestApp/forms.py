from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser, Household, Collector, CompostManager, Farmer
from MyApp.models import tbl_District, tbl_location, tbl_residentsassociation


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'required': True
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'required': True
        })
    )


class UserRegistrationForm(forms.ModelForm):
    """Base form for user registration with role selection"""
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'required': True
        }),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'required': True
        }),
        label="Confirm Password"
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'role']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
                'required': True
            }),
            'role': forms.Select(attrs={
                'id': 'id_role',
                'name': 'role',
                'style': 'width:100%;margin-top:8px;'
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class HouseholdRegistrationForm(forms.ModelForm):
    """Form for household-specific registration details"""
    aadhaar_image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'accept': 'image/*'
        }),
        label="Aadhaar Image"
    )

    class Meta:
        model = Household
        fields = ['household_name', 'phone', 'address', 'district', 'location', 
                 'residents_association', 'aadhaar_image']
        widgets = {
            'household_name': forms.TextInput(attrs={
                'placeholder': 'Household Name',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Address',
                'rows': 3,
                'required': True
            }),
            'district': forms.Select(attrs={
                'required': True
            }),
            'location': forms.Select(attrs={
                'required': True
            }),
            'residents_association': forms.Select(attrs={
                'required': True
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = tbl_District.objects.all()
        self.fields['location'].queryset = tbl_location.objects.all()
        self.fields['residents_association'].queryset = tbl_residentsassociation.objects.all()


class CollectorRegistrationForm(forms.ModelForm):
    """Form for collector-specific registration details"""
    license_image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'accept': 'image/*'
        }),
        label="License Image"
    )

    class Meta:
        model = Collector
        fields = ['collector_name', 'phone', 'address', 'license_image']
        widgets = {
            'collector_name': forms.TextInput(attrs={
                'placeholder': 'Collector Name',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Address',
                'rows': 3,
                'required': True
            })
        }


class CompostManagerRegistrationForm(forms.ModelForm):
    """Form for compost manager-specific registration details"""
    
    class Meta:
        model = CompostManager
        fields = ['compostmanager_name', 'phone', 'address', 'license_number']
        widgets = {
            'compostmanager_name': forms.TextInput(attrs={
                'placeholder': 'Compost Manager Name',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Address',
                'rows': 3,
                'required': True
            }),
            'license_number': forms.TextInput(attrs={
                'placeholder': 'License Number',
                'required': True
            })
        }

    def clean_license_number(self):
        license_number = self.cleaned_data.get('license_number')
        if CompostManager.objects.filter(license_number=license_number).exists():
            raise ValidationError("This license number is already registered.")
        return license_number


class FarmerRegistrationForm(forms.ModelForm):
    """Form for farmer-specific registration details"""
    aadhaar_image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'input-box',
            'accept': 'image/*'
        }),
        label="Aadhaar Image"
    )

    class Meta:
        model = Farmer
        fields = ['farmer_name', 'phone', 'address', 'aadhaar_image']
        widgets = {
            'farmer_name': forms.TextInput(attrs={
                'class': 'input-box',
                'placeholder': 'Farmer Name',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'input-box',
                'placeholder': 'Phone',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'class': 'input-box',
                'placeholder': 'Address',
                'rows': 3,
                'required': True
            })
        }


# Legacy form for backward compatibility (if needed)
class SignupForm(UserRegistrationForm):
    """Legacy signup form - redirects to UserRegistrationForm for compatibility"""
    mobile = forms.CharField(
        label="Mobile Number",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Mobile number'
        })
    )
    dob = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={
            'class': 'input-box',
            'type': 'date'
        }),
        required=False
    )
    place = forms.CharField(
        label="Place / City",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Your city'
        })
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")
        if not mobile:
            raise ValidationError("Mobile number is required.")
        return mobile