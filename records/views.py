from django.shortcuts import render
from .models import CustomUsers, Driver, Customer
from .serializers import CustomUsersSerializer, DriverSerializer, CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class driver(APIView):
    def get(self, request):
        driverUsers=Driver.objects.all()
        serializer2=DriverSerializer(driverUsers, many=True)
        return Response(serializer2.data)


class customer(APIView):
    def get(self, request, id=None):
        print(id)
        if(id==None):
            customerUsers=Customer.objects.all()
            serializer2=CustomerSerializer(customerUsers, many=True)
            return Response(serializer2.data)
        else:
            print("In else")
            customerobject=CustomUsers.objects.get(id=id)
            user_id=customerobject.id
            customerUsersParticular=Customer.objects.get(user_id=user_id)
            serializer2=CustomerSerializer(customerUsersParticular)
            return Response(serializer2.data)


# class customerID(APIView):
#     def get(self, request, abc):
#         print(request)
#         print (abc)
#         return Response(abc)


class driverCreation(APIView):
    def post(self, request):
        #Initialization of serializers.
        serializer1 = CustomUsersSerializer(data=request.data)
        serializer2=  DriverSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1Obj=serializer1.save()
            request.data["user"]=serializer1Obj.id
            #request.data gets updated and is passed into the serializer2
            if serializer2.is_valid():
                print(serializer1.validated_data)
                print("\n")
                print(serializer2.validated_data)
                print("\n")
                print("reques.data now is\n")
                print(request.data)
                serializer2.save()
                return Response(status=200)
            else:
                print("serializers2 in invalid")
                #Because serializer2 is invalid, we delete the instance of
                #serializer1 in the database
                serializer1Obj.delete();
                return Response(serializer2.errors, status=400)
        else:
            print("serializers1 in invalid")
            return Response(serializer1.errors, status=400)

class customerCreation(APIView):
    def post(self, request):
        serializer1 = CustomUsersSerializer(data=request.data)
        serializer2=CustomerSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1Obj=serializer1.save()
            request.data["user"]=serializer1Obj.id
            if serializer2.is_valid():
                print(serializer1.validated_data)
                print("\n")
                print(serializer2.validated_data)
                print("\n")
                print("reques.data now is\n")
                print(request.data)
                serializer2.save()
                return Response(status=200)
            else:
                print("serializers2 in invalid")
                #Because serializer2 is invalid, we delete the instance of
                #serializer1 in the database
                serializer1Obj.delete();
                return Response(serializer2.errors, status=400)
        else:
            print("serializers1 in invalid")
            return Response(serializer1.errors, status=400)
