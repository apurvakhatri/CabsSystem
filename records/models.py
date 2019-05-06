from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUsers(AbstractUser):
    DRIVER='DR'
    CUSTOMER='C'
    EMPLOYEE_CHOICES=(
        (DRIVER,'DRIVER'),
        (CUSTOMER, 'CUSTOMER')
    )
    country_code=models.PositiveIntegerField(null=True)
    contact_number=models.PositiveIntegerField(null=True)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pincode=models.PositiveIntegerField(null=True)
    type=models.CharField(max_length=2, choices=EMPLOYEE_CHOICES)

class Driver(models.Model):
    user=models.OneToOneField(CustomUsers, on_delete=models.CASCADE, primary_key=True, null=False)
    license_number=models.CharField(max_length=255)
    car_number=models.CharField(max_length=255)
    working=models.BooleanField(max_length=10, null=True)
    date_of_leaving=models.DateField(null=True)

class Customer(models.Model):
    user=models.OneToOneField(CustomUsers, on_delete=models.CASCADE, primary_key=True, null=False)
    Upi_id=models.CharField(max_length=255)
