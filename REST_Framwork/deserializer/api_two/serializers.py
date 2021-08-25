from rest_framework import serializers
from .models import Student
from django.db import models
from django.db.models import fields

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    
    def create(self,validate_data):
        return Student.objects.create(**validate_data)