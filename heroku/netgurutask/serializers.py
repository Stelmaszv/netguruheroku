from rest_framework import serializers
from .models import Car
class CarDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name','model','avg_rating']

class CarSerializerPopular(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'name','model','rates_number']
