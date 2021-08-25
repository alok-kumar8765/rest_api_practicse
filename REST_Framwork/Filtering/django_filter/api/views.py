from django.views import generic
from api.models import Students
from django.shortcuts import render
from .serializers import StudentsSerializer
from rest_framework.generics import ListAPIView
from .models import Students
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
# Create your views here.

class StudentsList(ListAPIView):
    #queryset = Students.objects.filter(passby = 'user1')
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'city')
    
    

'''
super
pass- super

user1
pass-admin@123

user2
pass-admin@123

to access use:- http://127.0.0.1:8000/studentapi/?name= any_name&city=any_city
'''