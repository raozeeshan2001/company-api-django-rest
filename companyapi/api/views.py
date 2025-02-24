from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Companyserializer
from .models import Company
# Create your views here.

class Companyviewset(viewsets.ModelViewSet):

    queryset=Company.objects.all()
    serializer_class=Companyserializer