from django.shortcuts import render
from .models import CustomUsers
from .serializers import CustomUsersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class driverCreation(APIView):
    def post(self, request):
        # print("In here")
        print(request.data)
        serializer = CustomUsersSerializer(data=request.data)
        print("\n serializer is\n")
        print(serializer)
        if serializer.is_valid():
            print("Is valid")
            serializer.save()
            return Response(serializer.data, status=200)
        print("Is invalid")
        return Response(serializer.errors, status=400)

# INSERT INTO CustomUsers (password, last_login, is_superuser, username,
# first_name, last_name, email, is_staff,
# is_active, date_joined, address, country_code, contact_number,
# country, city, state, pincode,
# type)
# VALUES (request.data["password"], request.data["last_login"], request.data["is_superuser"],request.data["username"],
# request.data["first_name"], request.data["last_name"], request.data["email"], request.data["is_staff"],
# request.data["is_active"], request.data["date_joined"], request.data["address"], request.data["country_code"]
# request.data["contact_number"], request.data["country"], request.data["city"], request.data["state"], request.data["pincode"]);



class customUserSignIn(APIView):

    def get(self, request):
        customUser=CustomUsers.objects.all()
        serializer=CustomUsersSerializer(customUser, many=True)
        return Response(serializer.data)
