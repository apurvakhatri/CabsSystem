from django.shortcuts import render
from .models import CustomUsers, Driver, Customer
from .serializers import CustomUsersSerializer, DriverSerializer, CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
import math
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
            customerUsersParticular=Customer.objects.get(user_id=id)
            serializer2=CustomerSerializer(customerUsersParticular)
            return Response(serializer2.data)

class book(APIView):
    def deg2rad(deg):
        return deg * (math.pi/180)

    def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2):
        R = 6371 #Radius of the earth in km
        dLat = book.deg2rad(lat2-lat1) # deg2rad below
        dLon = book.deg2rad(lon2-lon1)
        a = (math.sin(dLat/2) * math.sin(dLat/2))+(math.cos(book.deg2rad(lat1)) * math.cos(book.deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c # Distance in km
        return d

    def get(self, request, id, lat, lon):
        lat1=float(lat)
        lon1=float(lon)
        driverUsers=Driver.objects.all()
        serializer2=DriverSerializer(driverUsers, many=True)
        table1=[]
        table2=[]
        table3=[]
        for i in serializer2.data:
            if(i["status"]==True):
                table1.append(i)
        # print("table1 is \n")
        # print(table1)
        print("no_of_elements in table1 are:")
        print(len(table1))
        print("table1 is\n")
        print(table1)
        for i in table1:
            distance=book.getDistanceFromLatLonInKm(lat1, lon1, i["latitude"], i["longitude"])
            print("Distance is & id is\n")
            print(distance)
            print("\n")
            print(i["id"])
            if(distance<5):
                i["distance"]=distance
                table2.append(i)
        print("table2 is\n")
        print(table2)
        print("no_of_elements in table2 are:")
        print(len(table2))
        lower_bound=5
        while(len(table3)==0):
            lower_bound=lower_bound-0.5
            for i in table2:
                if(i["rating"]>lower_bound):
                    table3.append(i)
        min_distance=15.0
        rating_score=100.00
        print("table3 is\n")
        print(table3)
        for i in table3:
            if(distance<min_distance):
                min_distance=distance
                local_best=i
        print("local_best is\n")
        print(local_best)
        found=0
        for i in table3:
            if(i!=local_best):
                if(local_best["distance"]<i["distance"]<local_best["distance"]+2.0):
                    ind_rating_score=i["rating"]/i["distance"]
                    if(ind_rating_score<rating_score):
                        found=1
                        rating_score=ind_rating_score
                        global_best=i
        if(found==0):
            print("local_best is global_best & it is \n")
            print(local_best)
        else:
            print("global_best is\n")
            print(global_best)

class driverCreation(APIView):
    def post(self, request):
        # data=request.data
        #Initialization of serializers.
        request.data["id"]=uuid.uuid4()
        serializer1 = CustomUsersSerializer(data=request.data)
        # customerObj=CustomUsers.objects.get(username=data["username"])
        # request.data["id"]=customerObj["id"]
        serializer2=  DriverSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1Obj=serializer1.save()
            # customerObj=CustomUsers.objects.get(username=data["username"])
            # request.data["id"]=customerObj["id"]
            request.data["user"]=serializer1Obj.id
            # request.data["id"]=serializer1Obj.id

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
