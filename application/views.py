from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicationSerializers
from .models import ApplicationModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

@api_view(("GET",))
def deleteApplicationView(request,pk):
    try:
        data = ApplicationModel.objects.get(pk=pk)
        data.delete()
        return Response({"message":"application deleted"})
    except:
        return Response({"message":"No data found. Check your pk."})