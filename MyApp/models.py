from django.db import models
from MyApp.constants import (
    PAYMENT_STATUS_CHOICES, PAYMENT_STATUS_SIMPLE,
    DELIVERY_STATUS_CHOICES, PICKUP_STATUS_CHOICES,
    PAYMENT_METHOD_CHOICES, COMPOST_GRADE_CHOICES,
    COMPOST_STATUS_CHOICES, WASTE_STATUS_CHOICES,
    TRANSACTION_TYPE_CHOICES, TRANSACTION_STATUS_CHOICES,
    ORDER_ITEM_TYPE_CHOICES, ASSIGNMENT_STATUS_CHOICES
)


# System Settings Model
class SystemSettings(models.Model):
    """Store configurable system settings"""
    setting_key = models.CharField(max_length=100, unique=True, primary_key=True)
    setting_value = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "System Setting"
        verbose_name_plural = "System Settings"
    
    def __str__(self):
        return f"{self.setting_key}: {self.setting_value}"
    
    @classmethod
    def get_setting(cls, key, default=None):
        """Get a setting value by key"""
        try:
            return cls.objects.get(setting_key=key).setting_value
        except cls.DoesNotExist:
            return default
    
    @classmethod
    def set_setting(cls, key, value, description=""):
        """Set a setting value"""
        obj, created = cls.objects.update_or_create(
            setting_key=key,
            defaults={'setting_value': value, 'description': description}
        )
        return obj


# Create your models here.
class tbl_District(models.Model):
    District_id = models.AutoField(primary_key=True)
    District_Name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.District_Name
    
class tbl_location(models.Model):
    Location_id = models.AutoField(primary_key=True)
    Ward_No= models.IntegerField()
    Ward_Name= models.CharField(max_length=100)
    District = models.ForeignKey(tbl_District, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Ward_Name
    
class tbl_residentsassociation(models.Model):
    RA_id = models.AutoField(primary_key=True)
    Association_Name = models.CharField(max_length=200)
    Location = models.ForeignKey(tbl_location, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.Association_Name


class tbl_Route(models.Model):
    Route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(tbl_location, on_delete=models.CASCADE)
    residents_association = models.ForeignKey(tbl_residentsassociation, on_delete=models.CASCADE, null=True, blank=True)
    start_house_no = models.IntegerField(null=True, blank=True, verbose_name="Start House No")
    end_house_no = models.IntegerField(null=True, blank=True, verbose_name="End House No")

    def __str__(self):
        base = self.name
        if self.start_house_no and self.end_house_no:
            base += f" (Houses {self.start_house_no}-{self.end_house_no})"
        return base


class tbl_CollectorAssignment(models.Model):
    Assign_id = models.AutoField(primary_key=True)
    collector = models.ForeignKey('GuestApp.Collector', on_delete=models.CASCADE, verbose_name="Collector")
    Route_id = models.ForeignKey(tbl_Route, on_delete=models.CASCADE, verbose_name="Route")
    day_of_week = models.CharField(max_length=50, verbose_name="Day of Week")

    class Meta:
        verbose_name = "Collector Assignment"
        verbose_name_plural = "Collector Assignments"
        unique_together = ['collector', 'Route_id', 'day_of_week']

    def __str__(self):
        return f"{self.collector} - {self.Route_id} ({self.day_of_week})"

class tbl_BinType(models.Model):
    """Bin types with capacity and pricing"""
    BinType_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)  # "Medium" or "Large"
    capacity_kg = models.IntegerField()  # 25 or 50
    price_rs = models.DecimalField(max_digits=10, decimal_places=2)  # 50.00 or 100.00
    
    def __str__(self):
        return f"{self.name} ({self.capacity_kg}kg - ₹{self.price_rs})"

class tbl_HouseholdPayment(models.Model):
    """Track payments made by households for waste pickup service"""
    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]
    
    Payment_id = models.AutoField(primary_key=True)
    household = models.ForeignKey('GuestApp.Household', on_delete=models.CASCADE)
    bin_type = models.ForeignKey(tbl_BinType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_for_date = models.DateField()  # Which date this payment covers
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='Completed')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"Payment {self.Payment_id} - {self.household} - ₹{self.amount} ({self.payment_for_date})"

class tbl_PickupRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('UPI', 'UPI'),
        ('COD', 'Cash on Delivery'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    Pickup_id = models.AutoField(primary_key=True)
    household = models.ForeignKey('GuestApp.Household', on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    request_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    assigned_collector = models.ForeignKey('GuestApp.Collector', on_delete=models.CASCADE, null=True, blank=True)
    bin_type = models.ForeignKey(tbl_BinType, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(tbl_HouseholdPayment, on_delete=models.SET_NULL, null=True, blank=True)
    actual_weight_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Payment fields
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request {self.Pickup_id} - {self.household}"

class tbl_CollectionRequest(models.Model):
    Request_id = models.AutoField(primary_key=True)
    household = models.ForeignKey('GuestApp.Household', on_delete=models.CASCADE)
    collector = models.ForeignKey('GuestApp.Collector', on_delete=models.CASCADE)
    total_quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    farmer_supply_kg = models.DecimalField(max_digits=10, decimal_places=2)
    leftover_compost_kg = models.DecimalField(max_digits=10, decimal_places=2)
    collection_date = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Collection {self.Request_id} - {self.household}"


# NEW: Waste Inventory for Farmer Purchasing
class tbl_WasteInventory(models.Model):
    """Track available waste for farmer purchase before composting"""
    # Using imported WASTE_STATUS_CHOICES from constants.py
    
    Inventory_id = models.AutoField(primary_key=True)
    collection_request = models.ForeignKey(tbl_CollectionRequest, on_delete=models.CASCADE)
    collector = models.ForeignKey('GuestApp.Collector', on_delete=models.CASCADE)
    available_quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    collection_date = models.DateTimeField()
    expiry_date = models.DateTimeField(null=True, blank=True)  # Auto-calculated: collection_date + 30 days
    status = models.CharField(max_length=20, choices=WASTE_STATUS_CHOICES, default='Available')
    salary_paid = models.BooleanField(default=False)  # Track if collector salary paid for this date
    
    class Meta:
        ordering = ['-collection_date']
    
    def __str__(self):
        return f"Inventory {self.Inventory_id} - {self.available_quantity_kg}kg ({self.status})"


# MODIFIED: Farmer Supply with pricing and delivery fields
class tbl_FarmerSupply(models.Model):
    """Track direct waste supplied to farmers for animal feeding"""
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    ]
    
    DELIVERY_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    ]
    
    Supply_id = models.AutoField(primary_key=True)
    Farmer_id = models.ForeignKey('GuestApp.Farmer', on_delete=models.CASCADE)
    Collection_id = models.ForeignKey(tbl_CollectionRequest, on_delete=models.CASCADE, null=True, blank=True)
    Quantity = models.DecimalField(max_digits=10, decimal_places=2)
    Supply_Date = models.DateTimeField(auto_now_add=True)
    
    # NEW FIELDS
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    delivery_address = models.TextField()
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='Pending')
    Payment_id = models.ForeignKey('tbl_PaymentTransaction', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['-Supply_Date']
    
    def __str__(self):
        return f"Supply {self.Supply_id} - {self.Farmer_id.farmer_name} - {self.Quantity}kg"


# MODIFIED: Compost Batch with pricing
class tbl_CompostBatch(models.Model):
    """Compost batches from processed waste"""
    # Using imported COMPOST_STATUS_CHOICES from constants.py
    
    # Using imported COMPOST_GRADE_CHOICES from constants.py
    # Matches actual database data: Premium, A, B, C
    
    Batch_id = models.AutoField(primary_key=True)
    CompostManager_id = models.ForeignKey('GuestApp.CompostManager', on_delete=models.CASCADE)
    Batch_name = models.CharField(max_length=100)
    Source_Waste_kg = models.DecimalField(max_digits=10, decimal_places=2)
    Date_Created = models.DateField()
    Status = models.CharField(max_length=20, choices=COMPOST_STATUS_CHOICES, default='Processing')
    Grade = models.CharField(max_length=20, choices=COMPOST_GRADE_CHOICES, default='A')
    Stock_kg = models.DecimalField(max_digits=10, decimal_places=2)
    
    # NEW FIELD
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, default=200.00)
    salary_paid = models.BooleanField(default=False)  # Track if manager salary paid for this batch date
    
    class Meta:
        ordering = ['-Date_Created']
    
    def __str__(self):
        return f"{self.Batch_name} - {self.Grade} ({self.Stock_kg}kg @ ₹{self.price_per_kg}/kg)"


# Order and OrderItem models
class tbl_Order(models.Model):
    """Orders placed by farmers for waste or compost"""
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    ]
    
    Order_id = models.AutoField(primary_key=True)
    Buyer_id = models.ForeignKey('GuestApp.Farmer', on_delete=models.CASCADE)
    Order_Date = models.DateTimeField(auto_now_add=True)
    Total_Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Delivery_Address = models.TextField()
    Payment_Status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    
    # Manual Collector Assignment Fields
    assigned_collector = models.ForeignKey(
        'GuestApp.Collector',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_waste_orders'
    )
    assignment_status = models.CharField(
        max_length=20,
        choices=[
            ('Unassigned', 'Unassigned'),
            ('Assigned', 'Assigned')
        ],
        default='Unassigned'
    )
    
    class Meta:
        ordering = ['-Order_Date']
    
    def __str__(self):
        return f"Order {self.Order_id} - {self.Buyer_id.farmer_name} - ₹{self.Total_Amount}"


# MODIFIED: OrderItem to handle both waste and compost
class tbl_OrderItem(models.Model):
    """Items in an order - can be compost or direct waste"""
    ITEM_TYPE_CHOICES = [
        ('Compost', 'Compost'),
        ('Waste', 'Direct Waste'),
    ]
    
    DELIVERY_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    ]
    
    Item_id = models.AutoField(primary_key=True)
    Order_id = models.ForeignKey(tbl_Order, on_delete=models.CASCADE)
    Item_Type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    
    # MODIFIED: Made nullable to support both types
    Batch_id = models.ForeignKey(tbl_CompostBatch, on_delete=models.CASCADE, null=True, blank=True)
    FarmerSupply_id = models.ForeignKey(tbl_FarmerSupply, on_delete=models.CASCADE, null=True, blank=True)
    
    Quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    Unit_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Delivery_Status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='Pending')
    
    def __str__(self):
        return f"Item {self.Item_id} - {self.Item_Type} - {self.Quantity_kg}kg"


# Payment Transaction model
class tbl_PaymentTransaction(models.Model):
    """Track all payment transactions"""
    TRANSACTION_TYPE_CHOICES = [
        ('HouseholdDaily', 'Household Daily Payment'),
        ('CompostSale', 'Compost Sale'),
        ('WasteSale', 'Direct Waste Sale'),
        ('CollectorSalary', 'Collector Salary'),
        ('ManagerFee', 'Manager Processing Fee'),
    ]
    
    STATUS_CHOICES = [
        ('Success', 'Success'),
        ('Failed', 'Failed'),
        ('Pending', 'Pending'),
    ]
    
    Transaction_id = models.AutoField(primary_key=True)
    Payer_id = models.ForeignKey('GuestApp.CustomUser', on_delete=models.CASCADE, related_name='payments_made')
    Receiver_id = models.ForeignKey('GuestApp.CustomUser', on_delete=models.CASCADE, related_name='payments_received')
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=30, choices=TRANSACTION_TYPE_CHOICES)
    Reference_id = models.IntegerField(null=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Success')
    
    class Meta:
        ordering = ['-transaction_date']
    
    def __str__(self):
        return f"Transaction {self.Transaction_id} - {self.transaction_type} - ₹{self.Amount}"

