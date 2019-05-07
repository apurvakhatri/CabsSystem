from rest_framework import serializers
from .models import CustomUsers, Driver, Customer

class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUsers
        fields='__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driver
        fields="__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"
