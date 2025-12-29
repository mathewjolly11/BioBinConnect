from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from GuestApp.models import Household
from MyApp.models import tbl_Route
import json


@csrf_exempt
@require_http_methods(["POST"])
def validate_house_number(request):
    """
    API endpoint to validate house number against existing house numbers
    and route ranges to ensure the entered value is appropriate.
    """
    try:
        data = json.loads(request.body)
        house_no = data.get('house_no')
        district_id = data.get('district_id')
        location_id = data.get('location_id')
        residents_association_id = data.get('residents_association_id')
        current_household_id = data.get('current_household_id')  # For edit forms
        
        if not house_no:
            return JsonResponse({
                'valid': False,
                'message': 'House number is required'
            })
        
        try:
            house_no = int(house_no)
        except ValueError:
            return JsonResponse({
                'valid': False,
                'message': 'House number must be a valid number'
            })
        
        if house_no < 1:
            return JsonResponse({
                'valid': False,
                'message': 'House number must be greater than 0'
            })
        
        # Get existing house numbers in the same area
        filters = {}
        if district_id:
            filters['district_id'] = district_id
        if location_id:
            filters['location_id'] = location_id
        if residents_association_id:
            filters['residents_association_id'] = residents_association_id
        
        existing_households = Household.objects.filter(**filters)
        
        # Exclude current household if editing
        if current_household_id:
            existing_households = existing_households.exclude(id=current_household_id)
        
        existing_house_numbers = [
            h.house_no for h in existing_households 
            if h.house_no is not None
        ]
        
        # Check if house number already exists
        if house_no in existing_house_numbers:
            return JsonResponse({
                'valid': False,
                'message': f'House number {house_no} already exists in this area'
            })
        
        # Check route constraints if residents association is specified
        suggestions = []
        if residents_association_id:
            routes = tbl_Route.objects.filter(residents_association_id=residents_association_id)
            
            for route in routes:
                if (route.start_house_no is not None and 
                    route.end_house_no is not None):
                    
                    # Check if house number fits in this route range
                    if route.start_house_no <= house_no <= route.end_house_no:
                        # Check if there are existing houses in this range
                        route_houses = [
                            h for h in existing_house_numbers 
                            if route.start_house_no <= h <= route.end_house_no
                        ]
                        
                        if route_houses:
                            max_house_in_range = max(route_houses)
                            if house_no <= max_house_in_range:
                                next_available = max_house_in_range + 1
                                if next_available <= route.end_house_no:
                                    suggestions.append(next_available)
                                    return JsonResponse({
                                        'valid': False,
                                        'message': f'House number {house_no} or lower numbers are taken in this route. Try {next_available} or higher (up to {route.end_house_no})',
                                        'suggestion': next_available
                                    })
        
        # Check general area constraints
        if existing_house_numbers:
            max_existing = max(existing_house_numbers)
            if house_no <= max_existing:
                next_available = max_existing + 1
                return JsonResponse({
                    'valid': False,
                    'message': f'House number {house_no} or lower are already taken. Try {next_available} or higher',
                    'suggestion': next_available
                })
        
        # All checks passed
        return JsonResponse({
            'valid': True,
            'message': f'House number {house_no} is available'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'valid': False,
            'message': 'Invalid request data'
        })
    except Exception as e:
        return JsonResponse({
            'valid': False,
            'message': 'An error occurred while validating house number'
        })


@login_required
@require_http_methods(["GET"])
def get_next_house_number(request):
    """
    Get the next available house number for a specific area
    """
    district_id = request.GET.get('district_id')
    location_id = request.GET.get('location_id')
    residents_association_id = request.GET.get('residents_association_id')
    
    filters = {}
    if district_id:
        filters['district_id'] = district_id
    if location_id:
        filters['location_id'] = location_id
    if residents_association_id:
        filters['residents_association_id'] = residents_association_id
    
    existing_households = Household.objects.filter(**filters)
    existing_house_numbers = [
        h.house_no for h in existing_households 
        if h.house_no is not None
    ]
    
    if existing_house_numbers:
        next_number = max(existing_house_numbers) + 1
    else:
        next_number = 1
    
    # Check route constraints
    if residents_association_id:
        routes = tbl_Route.objects.filter(residents_association_id=residents_association_id)
        for route in routes:
            if (route.start_house_no is not None and 
                route.end_house_no is not None and
                route.start_house_no <= next_number <= route.end_house_no):
                break
        else:
            # If no route found for next_number, find the first available route
            for route in routes:
                if (route.start_house_no is not None and 
                    route.end_house_no is not None):
                    route_houses = [
                        h for h in existing_house_numbers 
                        if route.start_house_no <= h <= route.end_house_no
                    ]
                    if route_houses:
                        route_next = max(route_houses) + 1
                        if route_next <= route.end_house_no:
                            next_number = route_next
                            break
                    else:
                        next_number = route.start_house_no
                        break
    
    return JsonResponse({
        'next_house_number': next_number
    })