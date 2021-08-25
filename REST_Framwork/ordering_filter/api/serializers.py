from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id','name','roll','city','passby']