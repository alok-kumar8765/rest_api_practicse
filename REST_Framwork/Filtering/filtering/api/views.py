from api.models import Students
from django.shortcuts import render
from .serializers import StudentsSerializer
from rest_framework.generics import ListAPIView
from .models import Students
# Create your views here.

class StudentsList(ListAPIView):
    #queryset = Students.objects.filter(passby = 'user1')
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    def get_queryset(self):
        user = self.request.user
        return Students.objects.filter(passby = user)
    
'''
super
pass- super

user1
pass-admin@123

user2
pass-admin@123

jo user admin pannel me login krke api open krega us se related data show krega, means user1 ne kitne student pass kiya, 
ye janne ke liye user1 login krkr api open krna h
'''