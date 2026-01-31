from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import (
    LoginForm, UserRegistrationForm, HouseholdRegistrationForm,
    CollectorRegistrationForm, CompostManagerRegistrationForm, FarmerRegistrationForm
)

# Create your views here.
def index(request):
    return render(request, 'Guest/index.html')

def about(request):
    return render(request, 'Guest/booking.html')

def login_view(request):
    if request.method == 'POST':
        # Check form type to differentiate between login and registration forms
        form_type = request.POST.get('form_type')
        
        # Only process if this is actually a login form submission
        if form_type == 'login':
            # Handle Login
            login_form = LoginForm(request, data=request.POST)
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # Check if user is verified/approved by admin (skip check for superusers)
                    if not user.is_superuser and not user.is_verified:
                        messages.error(request, 'account_not_verified')
                        context = {
                            'login_form': LoginForm(),
                            'user_form': UserRegistrationForm(),
                            'household_form': HouseholdRegistrationForm(),
                            'collector_form': CollectorRegistrationForm(),
                            'compost_form': CompostManagerRegistrationForm(),
                            'farmer_form': FarmerRegistrationForm(),
                        }
                        return render(request, 'Guest/login.html', context)
                    
                    login(request, user)
                    # Handle admin login - redirect directly
                    if user.is_superuser:
                        return redirect('admin_index')
                    elif user.role == 'household':
                        return redirect('household_dashboard')
                    elif user.role == 'collector':
                        return redirect('collector_dashboard')
                    elif user.role == 'compost_manager':
                        return redirect('compost_manager_dashboard')
                    elif user.role == 'farmer':
                        return redirect('farmer_dashboard')
                    else:
                        return redirect('guest_index') # Fallback redirect
                else:
                    messages.error(request, 'Invalid username or password.')
            
            # If login invalid, return with errors
            if login_form.errors:
                for field, errors in login_form.errors.items():
                    for error in errors:
                        # Convert standard "__all__" errors (like invalid login) to a general message
                        if field == '__all__':
                            messages.error(request, error)
                        else:
                            messages.error(request, f"{error}")

            context = {
                'login_form': login_form,
                'user_form': UserRegistrationForm(),
                'household_form': HouseholdRegistrationForm(),
                'collector_form': CollectorRegistrationForm(),
                'compost_form': CompostManagerRegistrationForm(),
                'farmer_form': FarmerRegistrationForm(),
            }
            return render(request, 'Guest/login.html', context)
        
        # If not a login form submission, redirect to signup view for registration processing
        else:
            return redirect('signup')



    else:
        # For GET request, initialize all forms as empty with prefixes
        login_form = LoginForm()
        user_form = UserRegistrationForm()
        household_form = HouseholdRegistrationForm(prefix='household')
        collector_form = CollectorRegistrationForm(prefix='collector')
        compost_form = CompostManagerRegistrationForm(prefix='compost')
        farmer_form = FarmerRegistrationForm(prefix='farmer')
    
    context = {
        'login_form': login_form,
        'user_form': user_form,
        'household_form': household_form,
        'collector_form': collector_form,
        'compost_form': compost_form,
        'farmer_form': farmer_form,
    }
    
    return render(request, 'Guest/login.html', context)

    

def signup(request):
    """
    Handles user registration for all roles:
    Household, Collector, Compost Manager, Farmer.
    """
    if request.method == 'POST':
        # Debug: Print POST data to see what's being received
        print("=== DEBUG: POST Data ===")
        print(f"Role: {request.POST.get('role')}")
        print(f"All POST keys: {list(request.POST.keys())}")
        print("========================")
        
        # Prepare forms with POST data
        user_form = UserRegistrationForm(request.POST)
        role = request.POST.get('role')
        
        # Initialize role-specific form based on selection with prefix
        role_form = None
        if role == 'household':
            role_form = HouseholdRegistrationForm(request.POST, request.FILES, prefix='household')
        elif role == 'collector':
            role_form = CollectorRegistrationForm(request.POST, request.FILES, prefix='collector')
        elif role == 'compost_manager':
            role_form = CompostManagerRegistrationForm(request.POST, request.FILES, prefix='compost')
        elif role == 'farmer':
            role_form = FarmerRegistrationForm(request.POST, request.FILES, prefix='farmer')
            
        # Debug: Print form validation status
        print(f"User form valid: {user_form.is_valid()}")
        print(f"Role form valid: {role_form.is_valid() if role_form else 'No role form'}")
        if role_form and not role_form.is_valid():
            print(f"Role form errors: {role_form.errors}")
        print("========================")

        # Validate both forms
        if user_form.is_valid() and role_form and role_form.is_valid():
            # Custom validation: Check required fields based on role
            validation_errors = []
            
            # Get phone from user_form since it's there
            phone = (user_form.cleaned_data.get('phone') or '').strip()
            if not phone:
                validation_errors.append("Phone number is required.")
            
            if role == 'household':
                name = (role_form.cleaned_data.get('household_name') or '').strip()
                address = (role_form.cleaned_data.get('address') or '').strip()
                district = role_form.cleaned_data.get('district')
                location = role_form.cleaned_data.get('location')
                residents_association = role_form.cleaned_data.get('residents_association')
                
                if not name:
                    validation_errors.append("Household name is required.")
                if not address:
                    validation_errors.append("Address is required.")
                if not district:
                    validation_errors.append("District is required.")
                if not location:
                    validation_errors.append("Location is required.")
                if not residents_association:
                    validation_errors.append("Residents association is required.")
                    
            elif role == 'collector':
                name = (role_form.cleaned_data.get('collector_name') or '').strip()
                address = (role_form.cleaned_data.get('address') or '').strip()
                
                if not name:
                    validation_errors.append("Collector name is required.")
                if not address:
                    validation_errors.append("Address is required.")
                    
            elif role == 'compost_manager':
                name = (role_form.cleaned_data.get('compostmanager_name') or '').strip()
                address = (role_form.cleaned_data.get('address') or '').strip()
                license_number = (role_form.cleaned_data.get('license_number') or '').strip()
                
                if not name:
                    validation_errors.append("Compost manager name is required.")
                if not address:
                    validation_errors.append("Address is required.")
                if not license_number:
                    validation_errors.append("License number is required.")
                    
            elif role == 'farmer':
                name = (role_form.cleaned_data.get('farmer_name') or '').strip()
                address = (role_form.cleaned_data.get('address') or '').strip()
                
                if not name:
                    validation_errors.append("Farmer name is required.")
                if not address:
                    validation_errors.append("Address is required.")
            
            # If there are validation errors, show them and return
            if validation_errors:
                for error in validation_errors:
                    messages.error(request, error)
                
                context = {
                    'login_form': LoginForm(),
                    'user_form': user_form,
                    'household_form': role_form if role == 'household' else HouseholdRegistrationForm(prefix='household'),
                    'collector_form': role_form if role == 'collector' else CollectorRegistrationForm(prefix='collector'),
                    'compost_form': role_form if role == 'compost_manager' else CompostManagerRegistrationForm(prefix='compost'),
                    'farmer_form': role_form if role == 'farmer' else FarmerRegistrationForm(prefix='farmer'),
                    'show_register': True
                }
                return render(request, 'Guest/login.html', context)

            # Get the plain text password BEFORE saving (it gets hashed on save)
            plain_password = user_form.cleaned_data.get('password')

            # Save the user with the extracted name
            user = user_form.save(commit=False)
            user.name = name
            user.save()

            # Save the role-specific profile - commit=False to set user first
            profile = role_form.save(commit=False)
            profile.user = user
            
            # Ensure the data is actually set before saving
            if role == 'collector':
                profile.collector_name = name
                profile.phone = phone
                profile.address = address
            elif role == 'compost_manager':
                profile.compostmanager_name = name
                profile.phone = phone
                profile.address = address
                profile.license_number = license_number
            elif role == 'farmer':
                profile.farmer_name = name
                profile.phone = phone
                profile.address = address
            elif role == 'household':
                profile.household_name = name
                profile.phone = phone
                profile.address = address
                profile.district = district
                profile.location = location
                profile.district = district
                profile.location = location
                profile.residents_association = residents_association
                profile.house_no = role_form.cleaned_data.get('house_no')
            
            profile.save()
            
            # Send registration confirmation email to user with credentials
            try:
                from utils.email_service import send_registration_confirmation_email
                send_registration_confirmation_email(user, plain_password)
            except Exception as e:
                print(f"Registration email failed: {e}")
            
            # Send email notification to admin about new registration
            try:
                from utils.email_service import send_new_registration_alert
                send_new_registration_alert(user)
            except Exception as e:
                print(f"Admin notification failed: {e}")
            
            messages.success(request, 'signup_success')
            return redirect('login')
        else:
            # Registration failed, re-render login page with errors and show register panel
            messages.error(request, "Registration failed. Please correct the errors.")
            
            # If user_form has errors, add them to messages
            if user_form.errors:
                for field, errors in user_form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
            
            # If role_form has errors, add them
            if role_form and role_form.errors:
                for field, errors in role_form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")

            context = {
                'login_form': LoginForm(),
                'user_form': user_form, # Return form with errors
                'household_form': role_form if role == 'household' else HouseholdRegistrationForm(prefix='household'),
                'collector_form': role_form if role == 'collector' else CollectorRegistrationForm(prefix='collector'),
                'compost_form': role_form if role == 'compost_manager' else CompostManagerRegistrationForm(prefix='compost'),
                'farmer_form': role_form if role == 'farmer' else FarmerRegistrationForm(prefix='farmer'),
                'show_register': True  # Signal to template to show register panel
            }
            return render(request, 'Guest/login.html', context)
    
    # If GET request to /signup/, redirect to login page (or could render registration form directly)
    return redirect('login')

def logout_view(request):
    """Logout the user and redirect to login page"""
    logout(request)
    messages.success(request, 'logout_success')
    return redirect('login')

def services(request):
    """Display services page for guests"""
    return render(request, 'Guest/services.html')

def contact(request):
    """Display contact page for guests"""
    return render(request, 'Guest/contact.html')

def about_us(request):
    """Display about us page for guests"""
    return render(request, 'Guest/about.html')

def faq(request):
    """Display FAQ page for guests"""
    return render(request, 'Guest/faq.html')

def how_it_works(request):
    """Display how it works page for guests"""
    return render(request, 'Guest/how_it_works.html')

def validation_demo(request):
    """Display validation demonstration page"""
    return render(request, 'Guest/validation_demo.html')

def test_voice(request):
    """Test page for voice accessibility features"""
    return render(request, 'test_voice.html')
