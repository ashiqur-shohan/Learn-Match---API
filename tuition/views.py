from django.shortcuts import render
from rest_framework import viewsets,pagination
from .models import TuitionModel
from .serializers import TuitionSerializers
# Create your views here.


class TuitionPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = page_size
    max_page_size = 12


class TuitionViewset(viewsets.ModelViewSet):
    queryset = TuitionModel.objects.all()
    serializer_class = TuitionSerializers
    pagination_class = TuitionPagination