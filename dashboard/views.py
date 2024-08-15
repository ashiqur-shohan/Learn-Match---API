from django.shortcuts import render
from user.models import TeacherModel
from tuition.models import TuitionModel
from application.models import ApplicationModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class DashboardStatView(APIView):
    def get(self, request):
        total_teachers = TeacherModel.objects.count()
        data = {
            'total_teachers': TeacherModel.objects.count(),
            'total_applications': ApplicationModel.objects.count(),
            'live_tuition_jobs': TuitionModel.objects.filter(available=True).count(),
        }
        return Response(data, status=status.HTTP_200_OK)
