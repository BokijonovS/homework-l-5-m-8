from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Area, Apartment, Company
from .serializers import AreaSerializer, ApartmentSerializer, CompanySerializer
from rest_framework import permissions
from rest_framework import viewsets


class ApartmentAPIView(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AreaAPIView(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CompanyAPIView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]