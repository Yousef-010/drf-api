from django.shortcuts import render
from rest_framework import generics

from .models import Car
from .serializers import CarSerializer


class Car_infoListView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class Car_infoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer