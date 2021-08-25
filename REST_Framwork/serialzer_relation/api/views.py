from django.shortcuts import render
from .models import Singer, Songs
from .serializers import SongsSerializer, SingerSerializer
from rest_framework import viewsets

from api import serializers

# Create your views here.
class SingerViewSets(viewsets.ModelViewSet):
    
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer



class SongViewSets(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer