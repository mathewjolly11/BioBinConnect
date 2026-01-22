"""
Shared constants for BioBinConnect application
Centralizes all choice fields to avoid duplication
"""

# Payment Status Choices
PAYMENT_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('Failed', 'Failed'),
]

PAYMENT_STATUS_SIMPLE = [
    ('Pending', 'Pending'),
    ('Paid', 'Paid'),
]

# Delivery Status Choices
DELIVERY_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Dispatched', 'Dispatched'),
    ('Delivered', 'Delivered'),
]

# Pickup Request Status
PICKUP_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Completed', 'Completed'),
]

# Payment Method Choices
PAYMENT_METHOD_CHOICES = [
    ('UPI', 'UPI'),
    ('Cash', 'Cash'),
    ('Card', 'Card'),
    ('COD', 'Cash on Delivery'),
]

# Compost Grade Choices (matches actual database data)
COMPOST_GRADE_CHOICES = [
    ('Premium', 'Premium'),
    ('A', 'Grade A'),
    ('B', 'Grade B'),
    ('C', 'Grade C'),
]

# Compost Batch Status
COMPOST_STATUS_CHOICES = [
    ('Processing', 'Processing'),
    ('Ready', 'Ready'),
    ('Sold', 'Sold'),
]

# Waste Inventory Status
WASTE_STATUS_CHOICES = [
    ('Available', 'Available'),
    ('Sold', 'Sold to Farmer'),
    ('Expired', 'Expired'),
]

# Transaction Types
TRANSACTION_TYPE_CHOICES = [
    ('Household Payment', 'Household Payment'),
    ('Farmer Payment', 'Farmer Payment'),
    ('Collector Salary', 'Collector Salary'),
    ('Manager Salary', 'Manager Salary'),
    ('COD', 'Cash on Delivery'),
]

# Transaction Status
TRANSACTION_STATUS_CHOICES = [
    ('Success', 'Success'),
    ('Failed', 'Failed'),
    ('Pending', 'Pending'),
]

# Order Item Types
ORDER_ITEM_TYPE_CHOICES = [
    ('Compost', 'Compost'),
    ('Waste', 'Direct Waste'),
]

# Assignment Status
ASSIGNMENT_STATUS_CHOICES = [
    ('Unassigned', 'Unassigned'),
    ('Assigned', 'Assigned'),
]
