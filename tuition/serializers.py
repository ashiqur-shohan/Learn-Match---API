from rest_framework import serializers
from .models import TuitionModel

class TuitionSerializers(serializers.ModelSerializer):
    class Meta:
        model = TuitionModel
        fields = "__all__"