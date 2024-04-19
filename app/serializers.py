from rest_framework import serializers
from .models import RegistrationModel

class Regist_Serializer(serializers.ModelSerializer):
    class Meta:
        model=RegistrationModel
        fields= '__all__'