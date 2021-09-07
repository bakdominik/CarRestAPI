from django.db.models import Count, Avg

from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import CarSerializer, PopularSerializer, RateSerializer

from .models import Car, Rate
from .utils import model_exists, make_exists


@api_view(['GET', 'POST', 'DELETE'])
def cars(request,pk=None):
    if request.method == 'GET':
        cars = Car.objects.all().annotate(avg_rating=Avg('rate__rating'))
        return Response(CarSerializer(cars, many = True).data)

    elif request.method == 'POST':
        car_data = JSONParser().parse(request)
        car_serializer = CarSerializer(data=car_data)
        if car_serializer.is_valid(raise_exception=True):
            car_serializer.save()
            return Response(car_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def car_delete(request,pk):
    try: 
        car = Car.objects.get(pk=pk) 
    except Car.DoesNotExist: 
        return Response({'message': 'The car does not exist'}, status=status.HTTP_404_NOT_FOUND)
    car.delete()
    return Response({'message': 'Car was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def rate(request):
    rate_data = JSONParser().parse(request)
    rate_serializer = RateSerializer(data=rate_data)
    if rate_serializer.is_valid(raise_exception=True):
        rate_serializer.save()
        return Response(rate_serializer.data, status=status.HTTP_201_CREATED) 
    return Response(rate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def popular(request):
    cars = Car.objects.all().annotate(rates_number=Count('rate')).order_by('-rates_number')[:10]
    return Response(PopularSerializer(cars, many = True).data)

