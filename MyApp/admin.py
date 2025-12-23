from django.contrib import admin
from .models import tbl_District, tbl_location, tbl_residentsassociation, tbl_Route, tbl_CollectorAssignment

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
