from django.shortcuts import render

from rest_framework import generics
from .serializers import DressSerializer
from .models import Dress

class DressList(generics.ListCreateAPIView):
    queryset = Dress.objects.all().order_by('id')
    serializer_class = DressSerializer

class DressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dress.objects.all().order_by('id')
    serializer_class = DressSerializer
