from django.shortcuts import render
from rest_framework import viewsets
from .models import TuitionModel
from .serializers import TuitionSerializers
# Create your views here.

class TuitionViewset(viewsets.ModelViewSet):
    queryset = TuitionModel.objects.all()
    serializer_class = TuitionSerializers