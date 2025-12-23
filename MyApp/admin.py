from django.contrib import admin
from .models import (tbl_District, tbl_location, tbl_residentsassociation, 
                     tbl_Route, tbl_CollectorAssignment, tbl_BinType, 
                     tbl_HouseholdPayment, tbl_PickupRequest)

# Register your models here.

@admin.register(tbl_District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('District_id', 'District_Name')
    search_fields = ('District_Name',)

@admin.register(tbl_location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('Location_id', 'Ward_Name', 'Ward_No', 'District')
    list_filter = ('District',)
    search_fields = ('Ward_Name', 'Ward_No')

@admin.register(tbl_residentsassociation)
class ResidentsAssociationAdmin(admin.ModelAdmin):
    list_display = ('RA_id', 'Association_Name', 'Location')
    list_filter = ('Location__District', 'Location')
    search_fields = ('Association_Name',)

@admin.register(tbl_Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('Route_id', 'name', 'location')
    list_filter = ('location__District', 'location')
    search_fields = ('name',)

@admin.register(tbl_CollectorAssignment)
class CollectorAssignmentAdmin(admin.ModelAdmin):
    list_display = ('Assign_id', 'collector', 'Route_id', 'day_of_week')
    list_filter = ('day_of_week', 'Route_id__location', 'collector')
    search_fields = ('collector__collector_name', 'Route_id__name')

@admin.register(tbl_BinType)
class BinTypeAdmin(admin.ModelAdmin):
    list_display = ('BinType_id', 'name', 'capacity_kg', 'price_rs')
    search_fields = ('name',)

@admin.register(tbl_HouseholdPayment)
class HouseholdPaymentAdmin(admin.ModelAdmin):
    list_display = ('Payment_id', 'household', 'bin_type', 'amount', 'payment_for_date', 'payment_date', 'status', 'transaction_id')
    list_filter = ('status', 'payment_for_date', 'payment_date', 'bin_type')
    search_fields = ('household__household_name', 'transaction_id')
    date_hierarchy = 'payment_date'
    
    # Add actions for daily reports
    actions = ['generate_daily_report']
    
    def generate_daily_report(self, request, queryset):
        """Generate daily payment report"""
        from django.db.models import Sum, Count
        from django.contrib import messages
        
        total_amount = queryset.aggregate(Sum('amount'))['amount__sum'] or 0
        total_count = queryset.count()
        completed_count = queryset.filter(status='Completed').count()
        
        # Payment method breakdown
        upi_count = queryset.filter(status='Completed').count()  # Assuming all completed are from pickup requests
        
        message = f"""
        Daily Payment Report:
        - Total Payments: {total_count}
        - Completed: {completed_count}
        - Total Revenue: ₹{total_amount}
        """
        
        messages.success(request, message)
    
    generate_daily_report.short_description = "Generate Daily Payment Report"
    
    # Custom changelist view to show summary
    def changelist_view(self, request, extra_context=None):
        from django.db.models import Sum, Count
        from datetime import date
        
        # Get today's payments
        today = date.today()
        today_payments = tbl_HouseholdPayment.objects.filter(payment_date__date=today)
        
        # Calculate statistics
        today_total = today_payments.aggregate(Sum('amount'))['amount__sum'] or 0
        today_count = today_payments.count()
        today_completed = today_payments.filter(status='Completed').count()
        
        # All time statistics
        all_payments = tbl_HouseholdPayment.objects.all()
        all_total = all_payments.aggregate(Sum('amount'))['amount__sum'] or 0
        all_count = all_payments.count()
        
        extra_context = extra_context or {}
        extra_context['today_total'] = today_total
        extra_context['today_count'] = today_count
        extra_context['today_completed'] = today_completed
        extra_context['all_total'] = all_total
        extra_context['all_count'] = all_count
        
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(tbl_PickupRequest)
class PickupRequestAdmin(admin.ModelAdmin):
    list_display = ('Pickup_id', 'household', 'scheduled_date', 'bin_type', 'status', 'assigned_collector', 'payment')
    list_filter = ('status', 'scheduled_date', 'bin_type')
    search_fields = ('household__household_name', 'assigned_collector__collector_name')
    date_hierarchy = 'scheduled_date'
