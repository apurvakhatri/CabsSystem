from rest_framework import serializers
from .models import CustomUsers

class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUsers
        fields='__all__'

        # fields=('password','last_login','is_superuser','username',
        # 'first_name', 'last_name', 'email', 'is_staff', 'is_active',
        # 'date_joined', 'contact_number', 'country', 'state', 'city',
        # 'address', 'pincode', 'type', 'country_code')
