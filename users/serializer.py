from rest_framework import serializers
from .models import StudData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudData
        
        fields = '__all__'