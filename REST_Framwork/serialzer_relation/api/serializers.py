from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Singer, Songs

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'
class SingerSerializer(serializers.ModelSerializer):
    #song = serializers.StringRelatedField(many=True, read_only=True)
    #song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #song = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='song-detail')
    #song = serializers.SlugRelatedField(many=True, read_only=True,slug_field='title')
    song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']