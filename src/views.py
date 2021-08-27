from DjangoRestApiMongoDB.settings import DATABASES
from typing import cast
from django.shortcuts import render 
import json

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from src import serializers
 
from src.models import Tennis_court_1, Tennis_court_2, Tennis_court_3 #, Tutorial, Tennis_court
from src.serializers import CourtSerializer1, CourtSerializer2, CourtSerializer3 #, TutorialSerializer, CourtSerializer
from rest_framework.decorators import api_view
from datetime import datetime, date
import time
import re 

# Check the tennis court(day, date);
@api_view(['POST'])
def view_reserve_list(request, tennis_court):
    # recognize by tennis court
    if tennis_court == "1":
        model = Tennis_court_1
        serializer = CourtSerializer1
    elif tennis_court == "2":    
        model = Tennis_court_2
        serializer = CourtSerializer2
    elif tennis_court == "3":    
        model = Tennis_court_3
        serializer = CourtSerializer3
    else:
        return JsonResponse({"Error":"Not found tennis_court query"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Check the tennis court by day or date(2020-08-22)
    if request.method == 'POST':
        tennis_court = list(model.objects.all().values())
        data = JSONParser().parse(request)
        if data.get("day"):
            tennis_court = list(filter(lambda reservation: reservation["date_init"][0:10] == data["day"], tennis_court))
            return JsonResponse(tennis_court, safe=False) 
        elif data.get("client"):
            tennis_court = list(filter(lambda reservation: reservation["client"] == data["client"], tennis_court))
            return JsonResponse(tennis_court, safe=False) 
        else:
            return JsonResponse({"data":"no filter"}, safe=False)  

# data by tennis court all; Delete all data;
@api_view(['GET', 'DELETE'])
def tennis_reserve_all_list(request, tennis_court):
    # recognize by tennis court
    if tennis_court == "1":
        model = Tennis_court_1
        serializer = CourtSerializer1
    elif tennis_court == "2":    
        model = Tennis_court_2
        serializer = CourtSerializer2
    elif tennis_court == "3":    
        model = Tennis_court_3
        serializer = CourtSerializer3
    else:
        return JsonResponse({"Error":"Not found tennis_court query"}, status=status.HTTP_400_BAD_REQUEST)
    
    # return data by tennis court
    if request.method == 'GET':
        tennis_court = list(model.objects.all().values())
        title = request.GET.get('title', None)
        if title is not None:
            tennis_court = tennis_court.filter(title__icontains=title)
        
        tennis_court_serializer = serializer(tennis_court, many=True)
        return JsonResponse(tennis_court_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    # Delete one reservation, by reservation ID and client ID data
    elif request.method == 'DELETE':
        Data = JSONParser().parse(request)
        try: 
            reservation = model.objects.get(id=Data["id"]) 
            if Data["client"] == reservation.client:
                res = reservation.delete()
                return JsonResponse({'message': '{} Reservation of tennis court were deleted successfully!'.format(res[0])}, status=status.HTTP_202_ACCEPTED)
        except model.DoesNotExist: 
            print("Record doesn't exists")
            return JsonResponse({'message': 'the reservation doesn´t exist'}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({'message': 'The cliente Id is diffrent to reservation Id'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

# Update by client id; Create a reservation new;
@api_view(['PUT', 'POST'])
def client_data(request, tennis_court):
    # recognize by tennis court
    if tennis_court == "1":
        model = Tennis_court_1
        serializer = CourtSerializer1
    elif tennis_court == "2":    
        model = Tennis_court_2
        serializer = CourtSerializer2
    elif tennis_court == "3":    
        model = Tennis_court_3
        serializer = CourtSerializer3
    else:
        return JsonResponse({"Error":"Not found tennis_court query"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Update by client id
    if request.method == 'PUT':
        Data = JSONParser().parse(request) 
        try: 
            reservation = model.objects.get(id=Data["id"]) 
            print(type(reservation))
        except model.DoesNotExist: 
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
        change_reservation = serializer(reservation, data=Data) 
        if change_reservation.is_valid(): 
            change_reservation.save()
            print("guardado")
            return JsonResponse(change_reservation.data) 
        return JsonResponse(change_reservation.errors, status=status.HTTP_400_BAD_REQUEST) 

    # Create a reservation new
    elif request.method == 'POST':
            Data = JSONParser().parse(request)
            tutorial_serializer = serializer(data=Data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def verify_serve(request):
    if request.method == 'GET':
        return JsonResponse({'Serve': 'Running'}, safe=False)