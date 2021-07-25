from typing import List
from django.shortcuts import render
from rest_framework import viewsets
from .models import Listings
from .serializers import  ListingsSerializer

class Listings(viewsets.ModelViewSet):
    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer