from django.shortcuts import render
from .models import TuitionModel
from .serializers import TuitionSerializers
from rest_framework import viewsets,pagination,filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class TuitionPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = page_size
    max_page_size = 12


class TuitionViewset(viewsets.ModelViewSet):
    queryset = TuitionModel.objects.all()
    serializer_class = TuitionSerializers
    # pagination_class = TuitionPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    search_fields = ['grade','address']
    ordering_fields = ['salary']
    filterset_fields = ['grade_slug', 'tuition_type','location']
    def get_queryset(self):
        queryset = super().get_queryset()
        tuition_id = self.request.query_params.get("tuition_id")
        if tuition_id:
            queryset = queryset.filter(id = tuition_id)
        return queryset