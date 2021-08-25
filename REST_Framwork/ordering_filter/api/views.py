from api.models import Students
from django.shortcuts import render
from .serializers import StudentsSerializer
from rest_framework.generics import ListAPIView
from .models import Students
from rest_framework.filters import OrderingFilter
# Create your views here.

class StudentsList(ListAPIView):
    #queryset = Students.objects.filter(passby = 'user1')
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    filter_backends = [OrderingFilter]
    #ordering_fields = ['name'] #if this will not use the ordering will done by id,name,city,roll,passby, but her we
                                #specify to order with only name 
    ordering_fields = ['name','city']
'''
super
pass- super

user1
pass-admin@123

user2
pass-admin@123

'''