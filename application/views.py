from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicationSerializers
from .models import ApplicationModel
# Create your views here.

class ApplicationViewset(viewsets.ModelViewSet):
    queryset = ApplicationModel.objects.all()
    serializer_class = ApplicationSerializers


    # /?teacher_id=1 -- eivhabe search korle shudhu oi id er teacher er application gulo dekhabe
    def get_queryset(self):
        queryset =  super().get_queryset()
        teacher_id = self.request.query_params.get('teacher_id')
        tuition_id = self.request.query_params.get('tuition_id')
        if teacher_id:
            queryset = queryset.filter(teacher_id=teacher_id)
        if tuition_id:
            queryset = queryset.filter(tuition_id=tuition_id)
        return queryset
    