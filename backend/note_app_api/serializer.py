from rest_framework import serializers
from . import models

class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'
        
        
class Task_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['title','description']
