from rest_framework import serializers
from .models import Word
from django.db import models
from django.db.models import fields
from rest_framework import serializers

class WordSerializer(serializers.ModelSerializer):
    """Serializes the Word"""
    class Meta:
        model = Word
        fields = '__all__'
        
class WordsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    meanings = serializers.CharField()
    example = serializers.CharField()
    
    