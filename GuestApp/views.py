from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
        # Differentiate between login and registration forms
        if 'form_type' in request.POST and request.POST['form_type'] == 'register':
            # Handle Registration
            user_form = UserRegistrationForm(request.POST)
            role = request.POST.get('role')
            
            role_form = None
            if role == 'household':
                role_form = HouseholdRegistrationForm(request.POST, request.FILES)
            elif role == 'collector':
                role_form = CollectorRegistrationForm(request.POST, request.FILES)
            elif role == 'compost':
                role_form = CompostManagerRegistrationForm(request.POST, request.FILES)
            elif role == 'farmer':
                role_form = FarmerRegistrationForm(request.POST, request.FILES)

            if user_form.is_valid() and role_form and role_form.is_valid():
                # Get the name from the role-specific form
                name = ""
                if role == 'household':
                    name = role_form.cleaned_data.get('household_name')
                elif role == 'collector':
                    name = role_form.cleaned_data.get('collector_name')
                elif role == 'compost':
                    name = role_form.cleaned_data.get('compostmanager_name')
                elif role == 'farmer':
                    name = role_form.cleaned_data.get('farmer_name')

                # Save the user with the extracted name
                user = user_form.save(commit=False)
                user.name = name
                user.save()

                # Save the role-specific profile
                profile = role_form.save(commit=False)
                profile.user = user
                profile.save()
                
                messages.success(request, 'Registration successful! Please login.')
                return redirect('login_view')
            else:
                # Pass forms with errors back to the template
                login_form = LoginForm(request)
                # Add errors to messages framework to be displayed
                if user_form.errors:
                    for field, error in user_form.errors.items():
                        messages.error(request, f"{field}: {error}")
                if role_form and role_form.errors:
                    for field, error in role_form.errors.items():
                        messages.error(request, f"{field}: {error}")

        else:
            # Handle Login
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect based on user role
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
            # Initialize empty registration forms for the template
            user_form = UserRegistrationForm()
            household_form = HouseholdRegistrationForm()
            collector_form = CollectorRegistrationForm()
            compost_form = CompostManagerRegistrationForm()
            farmer_form = FarmerRegistrationForm()

    else:
        # For GET request, initialize all forms as empty
        login_form = LoginForm()
        user_form = UserRegistrationForm()
        household_form = HouseholdRegistrationForm()
        collector_form = CollectorRegistrationForm()
        compost_form = CompostManagerRegistrationForm()
        farmer_form = FarmerRegistrationForm()
    
    context = {
        'login_form': login_form,
        'user_form': user_form,
        'household_form': household_form,
        'collector_form': collector_form,
        'compost_form': compost_form,
        'farmer_form': farmer_form,
    }
    
    return render(request, 'Guest/login.html', context)