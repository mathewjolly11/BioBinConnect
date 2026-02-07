import os
import django
import sys
from django.db.models import Sum

# Add current directory to path
sys.path.append(os.getcwd())

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')
django.setup()

from MyApp.models import tbl_WasteInventory

def verify_stock_logic():
    print("--- Verifying Stock Calculation Logic ---")
    
    # 1. Calculate Old Logic (Available + Used)
    old_total = tbl_WasteInventory.objects.filter(status__in=['Available', 'Used']).aggregate(
            total=Sum('available_quantity_kg'))['total'] or 0
    print(f"Old Logic (Available + Used): {old_total} kg")
    
    # 2. Calculate New Logic (Available Only)
    new_total = tbl_WasteInventory.objects.filter(status='Available').aggregate(
            total=Sum('available_quantity_kg'))['total'] or 0
    print(f"New Logic (Available Only):   {new_total} kg")
    
    print("\nThe UI should now display the New Logic value.")

if __name__ == "__main__":
    verify_stock_logic()
