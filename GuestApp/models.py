from django.db import models
from MyApp.models import  tbl_District, tbl_location, tbl_residentsassociation


# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        return self.create_user(email, name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('household', 'Household'),
        ('collector', 'Collector'),
        ('compost_manager', 'Compost Manager'),
        ('farmer', 'Farmer'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=191, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='household')
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email 
    
class Household(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    household_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    aadhaar_image = models.ImageField(upload_to='household_aadhaar_images/')
    district = models.ForeignKey(tbl_District, on_delete=models.CASCADE)
    location = models.ForeignKey(tbl_location, on_delete=models.CASCADE)
    residents_association = models.ForeignKey(
        tbl_residentsassociation,
        on_delete=models.CASCADE
    )
    house_no = models.IntegerField(verbose_name="House Number", null=True, blank=True)
    registered_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return self.household_name
    
class Collector(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    collector_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    license_image = models.ImageField(upload_to='collector_licenses/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.collector_name
    



class CompostManager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    compostmanager_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=100)  # Added missing address field for consistency
    license_number = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.compostmanager_name
    
class Farmer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    farmer_name = models.CharField(max_length=100)
    aadhaar_image = models.ImageField(upload_to='farmer_aadhaar_images/')
    phone = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.farmer_name