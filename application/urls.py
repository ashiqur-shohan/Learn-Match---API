from rest_framework.routers import DefaultRouter
from django.urls import include,path
from .views import ApplicationViewset


router = DefaultRouter()

router.register('',ApplicationViewset)

urlpatterns = [
    path('',include(router.urls)),
]
