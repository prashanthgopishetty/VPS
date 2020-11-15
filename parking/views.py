from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ParkingSlot
from .serializers import ParkingSlotSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def parking_slots(request, format=None):
    if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            parkingslot = ParkingSlot.objects.filter(email=email)
        else:
            parkingslot = ParkingSlot.objects.all()
        serializer = ParkingSlotSerializer(parkingslot, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ParkingSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        email = request.GET.get('email')
        if email:
            person = ParkingSlot.objects.get(email=email)
            serializer = ParkingSlotSerializer(person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        email = request.GET.get('email')
        person = ParkingSlot.objects.filter(email=email)
        if person:
            person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
