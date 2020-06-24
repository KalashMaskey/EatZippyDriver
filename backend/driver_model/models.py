from django.db import models
from .validators import validate_file_size
from datetime import date
from django.conf import settings
# Create your models here.

class DriverDetail(models.Model):
    full_name = models.CharField(max_length=56)
    email = models.EmailField()
    contact = models.DecimalField(decimal_places=0, max_digits=15, default=977)
    dob = models.DateField(auto_now=False,auto_now_add=False,max_length=8)
    address = models.CharField(max_length=82,null=True)

    vehicle_no = models.CharField(max_length=26,null=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('B', 'Both'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)

    LICENSE_TYPE_CHOICES = (
        ('B', 'Bike'),
        ('S', 'Scooter'),
    )
    license_type = models.CharField(max_length=1, choices=LICENSE_TYPE_CHOICES,null=True)

    license_no = models.CharField(max_length=26,null=True)
    license_issue_office = models.CharField(max_length=82,null=True)
    license_expiray_date = models.DateField(auto_now=False,auto_now_add=False,max_length=8,null=True)

    STATUS_CHOICES = (
        ('S' , 'Single'),
        ('M' , 'Married'),
    )

    martial_status = models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)
    pan_no = models.DecimalField(decimal_places=0, max_digits=15)
    citizenship_no = models.DecimalField(decimal_places=0, max_digits=15)

    driving_license_file = models.FileField(upload_to='static_driver/', null=True, blank=False, validators=[validate_file_size])
