import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUsers(AbstractUser):
    DRIVER='DR'
    CUSTOMER='C'
    EMPLOYEE_CHOICES=(
        (DRIVER,'DRIVER'),
        (CUSTOMER, 'CUSTOMER')
    )
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address=models.CharField(max_length=100)
    country_code=models.PositiveIntegerField(null=True)
    contact_number=models.PositiveIntegerField(null=True)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.PositiveIntegerField(null=True)
    type=models.CharField(max_length=2, choices=EMPLOYEE_CHOICES)

class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user=models.OneToOneField(CustomUsers, on_delete=models.CASCADE, null=False)
    license_number=models.CharField(max_length=255)
    car_number=models.CharField(max_length=255)
    working=models.BooleanField(max_length=10, null=True)
    date_of_leaving=models.DateField(null=True)
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)
    status=models.BooleanField(max_length=10)
    rating=models.FloatField(default=1.0)

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user=models.OneToOneField(CustomUsers, on_delete=models.CASCADE, null=False)
    Upi_id=models.CharField(max_length=255)
