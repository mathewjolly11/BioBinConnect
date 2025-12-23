from django.db import models


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
    collector = models.ForeignKey('GuestApp.Collector', on_delete=models.CASCADE)
    Route_id = models.ForeignKey(tbl_Route, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=50)

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

